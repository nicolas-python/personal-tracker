from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify     #jsonify = Wandelt Python-Daten, beispielsweise ein Dictionary, in eine JSON-HTTP-Antwort um
from database import create_database, add_user, login_user, save_workout, update_workout, get_workouts, get_workout_exercises, get_workout , delete_workout, get_calorie_needs, save_calorie_needs, save_food, get_food, delete_food, update_food
import os                           #Operating System = Python-Modul für Funktionen des Betriebssystems
import sqlite3
import requests              # Python-Bibliothek zum Senden von HTTP-Anfragen an externe APIs
from http import HTTPStatus  # Enthält benannte HTTP-Statuscodes

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
    if "user_id" not in session:
        return redirect(url_for("login"))
    calorie_needs = get_calorie_needs(session["user_id"])

    return render_template("nutrition.html",calorie_needs=calorie_needs)

@app.route("/search-food")
def search_food():
    search_term = request.args.get("q", "").strip()     #Suchbegriff aus der URL auslesen, q = von Open Food Facts vorgegebener Parameter für den Suchbegriff

    if not search_term:
        return jsonify({"error": "Bitte ein Lebensmittel eingeben."}), HTTPStatus.BAD_REQUEST  #HTTP 400: Anfrage ungültig

    try:
        #Open Food Facts nach dem Lebensmittel fragen
        response = requests.get("https://search.openfoodfacts.org/search",
            params=[
                ("q", search_term),                 # q = von Open Food Facts vorgegebener Parameter für den Suchbegriff
                ("langs", "de:en"),              #deutsch bevorzugen, englisch zusätzlich berücksichtigen
                ("page_size", 100)                    #max 100 Ergebnisse anfordern fürs filtern #max fünf Ergebnisse anfordern
            ],
            headers={"User-Agent": "PersonalTracker/1.0"},timeout=10)

        response.raise_for_status()

        #Suchergebnisse als JSON an unsere Anwendung zurückgeben
        return jsonify(response.json())

    except requests.RequestException:
        return jsonify({"error": "Die Lebensmittelsuche ist momentan nicht erreichbar."}), HTTPStatus.BAD_GATEWAY  #HTTP 502: Server konnte keine gültige Antwort vom externen Dienst erhalten

    except ValueError:
        return jsonify({"error": "Die API hat ungültige Daten zurückgegeben."}), 502

@app.route("/save-calorie-needs", methods=["POST"])
def save_calorie_needs_route():
    if "user_id" not in session:
        return jsonify({"error": "Nicht angemeldet"}), 401

    data = request.get_json()

    save_calorie_needs(session["user_id"],data["calories"],data["protein"])

    return jsonify({"success": True})

@app.route("/save-food", methods=["POST"])
def save_food_route():
    if "user_id" not in session:
        return jsonify({"error": "Nicht angemeldet"}), 401

    data = request.get_json()

    save_food(
        session["user_id"],
        data["food_name"],
        data["grams"],
        data["calories"],
        data["protein"],
        data["fat"],
        data["carbs"],
        data["sugar"],
        data["meal"],
        data["entry_date"]
    )

    return jsonify({"success": True})

@app.route("/get-food")
def get_food_route():
    if "user_id" not in session:
        return jsonify({"error": "Nicht angemeldet"}), 401

    entry_date = request.args.get("date")

    if not entry_date:
        return jsonify({"error": "Datum fehlt"}), 400

    foods = get_food(session["user_id"], entry_date)

    return jsonify({"foods": foods})


@app.route("/delete-food", methods=["POST"])
def delete_food_route():
    if "user_id" not in session:
        return jsonify({"error": "Nicht angemeldet"}), 401

    data = request.get_json()
    food_id = data.get("food_id")

    if not food_id:
        return jsonify({"error": "Lebensmittel-ID fehlt"}), 400

    deleted_rows = delete_food(session["user_id"], food_id)

    if deleted_rows == 0:
        return jsonify({"error": "Lebensmittel nicht gefunden"}), 404

    return jsonify({"success": True})

@app.route("/update-food", methods=["POST"])
def update_food_route():
    if "user_id" not in session:
        return jsonify({"error": "Nicht angemeldet"}), 401

    data = request.get_json()
    food_id = data.get("food_id")

    required_fields = ["grams", "calories", "protein", "fat", "carbs", "sugar"]
    if not food_id or any(field not in data for field in required_fields):
        return jsonify({"error": "Daten fehlen"}), 400

    updated_rows = (update_food
        (
        session["user_id"],
        food_id,
        data["grams"],
        data["calories"],
        data["protein"],
        data["fat"],
        data["carbs"],
        data["sugar"]
        ))

    if updated_rows == 0:
        return jsonify({"error": "Lebensmittel nicht gefunden"}), 404

    return jsonify({"success": True})



if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5001, debug=False)