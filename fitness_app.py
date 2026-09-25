from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    return "Login wurde abgeschickt"


if __name__ == "__main__":
    app.run(debug=True)