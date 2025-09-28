from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    app.run(debug=True)