from flask import Flask, render_template, request, flash, session, redirect, url_for
from database import create_database, add_user, login_user, save_workout, update_workout, get_workouts, get_workout_exercises, get_workout ,delete_workout
import os                           #Operating System = Python-Modul für Funktionen des Betriebssystems
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")       #liest die Umgebungsvariable SECRET_KEY aus
                                                    #flash verlangt einen secret_key, um zu funktionieren
                                                    #Flask Secret Key = geheimer Schlüssel für Sessions und Flash-Nachrichten ,nicht mit dem Benutzerpasswort verwechseln!

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]

        if not username or not password or not password_confirm:
            flash("Bitte alle Felder ausfüllen", "error")
            return render_template("register.html")

        if password != password_confirm:
            flash("Die Passwörter stimmen nicht überein", "error")
            return render_template("register.html")

        try:
            add_user(username, password)
            flash("Registrierung erfolgreich!","success")  # flash = Flask-Funktion, mit der man eine kurze Nachricht über einen Seitenwechsel hinweg speichern und anzeigen kann

        except sqlite3.IntegrityError:
            flash("Der Benutzername ist bereits vergeben", "error")

    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if not username or not password:
        flash("Bitte Benutzername und Passwort eingeben", "error")
        return render_template("login.html")

    user = login_user(username, password)
    if user:
        session["user_id"] = user[0]
        flash("Login erfolgreich!", "success")              #flash(Nachricht, Kategorie) = Kategorie gibt an, um welche Art von Nachricht es sich handelt

    else:
        flash("Login fehlgeschlagen: Passwort oder Benutzername falsch", "error")

    return render_template("login.html")

@app.route("/selection")
def selection():
    return render_template("selection.html")


@app.route("/fitness")
def fitness():
    return render_template("fitness.html")

@app.route("/create-workout", methods=["GET", "POST"])
def create_workout():
    if request.method == "POST":
        workout_name = request.form["workout_name"]
        exercises = []

        for key in request.form:
            if "Exercise" in key and request.form[key]:
                exercise = request.form[key]

                sets = request.form[key.replace("Exercise", "Sets")]
                reps = request.form[key.replace("Exercise", "Reps")]
                weight = request.form[key.replace("Exercise", "Weight")]

                exercises.append((exercise, sets, reps, weight))

        save_workout(session["user_id"], workout_name, exercises)

        flash("Trainingsplan gespeichert!", "success")
        return render_template("create_workout.html", exercises=[], saved=True)

    return render_template("create_workout.html", exercises=[])

@app.route("/workouts")
def workouts():
    workouts = get_workouts(session["user_id"])
    workout_exercises = {}

    for workout in workouts:
        workout_id = workout[0]
        workout_exercises[workout_id] = get_workout_exercises(workout_id)

    return render_template("workouts.html",workouts=workouts,workout_exercises=workout_exercises)

@app.route("/edit-workout/<int:workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    if request.method == "POST":
        workout_name = request.form["workout_name"]
        exercises = []

        for key in request.form:
            if "Exercise" in key and request.form[key]:
                exercise = request.form[key]

                sets = request.form[key.replace("Exercise", "Sets")]
                reps = request.form[key.replace("Exercise", "Reps")]
                weight = request.form[key.replace("Exercise", "Weight")]

                exercises.append((exercise, sets, reps, weight))

        update_workout(workout_id, workout_name, exercises)

        flash("Trainingsplan aktualisiert!", "success")

        workout = get_workout(workout_id)
        exercises = get_workout_exercises(workout_id)

        return render_template("create_workout.html", workout=workout, exercises=exercises)

    workout = get_workout(workout_id)
    exercises = get_workout_exercises(workout_id)

    return render_template("create_workout.html", workout=workout, exercises=exercises)

@app.route("/delete-workout/<int:workout_id>", methods=["POST"])
def delete_workout_route(workout_id):
    # Prüfen, ob ein Benutzer angemeldet ist
    if "user_id" not in session:
        flash("Bitte melde dich zuerst an.", "error")
        return redirect(url_for("home"))                                    #url_for() sucht anhand des Funktionsnamens die passende URL heraus

    #trainingsplan löschen wen er dem Benutzer gehört
    deleted = delete_workout(workout_id, session["user_id"])

    if deleted:
        flash("Trainingsplan erfolgreich gelöscht!", "success")
    else:
        flash("Trainingsplan nicht gefunden.", "error")

    return redirect(url_for("workouts"))                                    #redirect() schickt den Browser anschließend zu dieser URL
@app.route("/start-workout/<int:workout_id>")               #id
def start_workout(workout_id):
    workout = get_workout(workout_id)
    exercises = get_workout_exercises(workout_id)

    return render_template("start_workout.html", workout=workout, exercises=exercises)


@app.route("/nutrition")
def nutrition():
    return render_template("nutrition.html")



if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5001, debug=False)