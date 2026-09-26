from flask import Flask, render_template, request, flash
from database import create_database, add_user

app = Flask(__name__)
app.secret_key = "dein-geheimer-schluessel"         #flash verlangt einen secret_key, um zu funktionieren
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
    return "Login wurde abgeschickt"


if __name__ == "__main__":
    create_database()
    app.run(debug=True)