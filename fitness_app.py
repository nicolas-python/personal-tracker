from flask import Flask, render_template, request
from database import add_user

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        add_user(username, password)

    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    return "Login wurde abgeschickt"


if __name__ == "__main__":
    app.run(debug=True)