from flask import Flask, render_template, request, flash
from database import create_database, add_user, login_user

app = Flask(__name__)
app.secret_key = "geheimer-schluessel"         #flash verlangt einen secret_key, um zu funktionieren
                                                    #Flask Secret Key = geheimer Schlüssel für Sessions und Flash-Nachrichten ,nicht mit dem Benutzerpasswort verwechseln!

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        add_user(username, password)
        flash("Registrierung erfolgreich!")     #flash = Flask-Funktion, mit der man eine kurze Nachricht über einen Seitenwechsel hinweg speichern und anzeigen kann

    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if login_user(username, password):
        return "Login wurde abgeschickt"

    else:
        return "Login Fehlgeschlagen: Passwort oder Benutzername falsch"



if __name__ == "__main__":
    create_database()
    app.run(debug=True)