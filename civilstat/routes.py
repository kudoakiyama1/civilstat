from flask import render_template

from civilstat import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register")
def register():
    return render_template("register.html")