from flask import Flask, render_template, redirect, request, url_for, session
import random
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
    {"question": "Who developed Python?", "answer": "Guido van Rossum"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "What is the speed of light?", "answer": "299,792 km/s"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the square root of 64?", "answer": "8"},
]

@app.route("/")
def index():
    session["cards"] = random.sample(flashcards, len(flashcards))
    session["current"] = 0
    session["correct"] = 0
    session["incorrect"] = 0
    return render_template("index.html")

@app.route("/card", methods=["GET","POST"])
def card():
    if session["current"] >= len(session["cards"]):
        return redirect(url_for("result"))

    card = session["cards"][session["current"]]
    return render_template("card.html", card=card)

@app.route("/answer", methods=["POST"])
def answer():
    result = request.form["result"]
    if result == "correct":
        session["correct"] += 1
    else:
        session["incorrect"] += 1

    session["current"] += 1
    return redirect(url_for("card"))

@app.route("/result")
def result():
    total = len(session["cards"])
    correct = session.get("correct", 0)
    incorrect = session.get("incorrect", 0)
    return render_template("result.html", total=total, correct=correct, incorrect=incorrect)


if __name__ == "__main__":
    app.run(debug=True)

