from flask import Flask, render_template, redirect, url_for, request, session
from quiz_data import quiz_questions
import random
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

class Question:
    def __init__(self, question_text, correct_answer, incorrect_answers):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.options = incorrect_answers+[correct_answer]
        random.shuffle(self.options)


questions = [Question(q["question"],q["correct_answer"],q["incorrect_answers"]) for q in quiz_questions]



@app.route("/")
def index():
    session["score"] = 0
    session["current"] = 0
    session.pop("feedback",None)
    return render_template("index.html")

@app.route("/question", methods=["GET","POST"])
def question():
    if request.method == "POST":
        selected = request.form.get("answer")
        current_q = session["current"]
        correct_answer = questions[current_q - 1].correct_answer
        if session["current"] < len(questions):
            if selected == correct_answer:
                session["score"] += 1
                session["feedback"] = "Correct..."
            else:
                session["feedback"] = f"Wrong.\nCorrect answer is: {correct_answer}"
        else:
            if selected == correct_answer:
                session["score"] += 1
                session["final_feedback"] = "Correct..."
            else:
                session["final_feedback"] = f"Wrong.\nCorrect answer is: {correct_answer}"
            
    if session["current"] >= len(questions):
        return redirect(url_for("result"))

    q = questions[session["current"]]
    session["current"] += 1
    progress = int((session["current"]/len(questions))*100)
    feedback = session.pop("feedback", None)
    return render_template("question.html", question=q, q_num=session["current"], total=len(questions), progress=progress, feedback=feedback)

@app.route("/result")
def result():
    score = session.get("score",0)
    total = len(questions)

    with open("score_log.txt", "a", encoding="utf-8") as fp:
        fp.write(f"Score: {score}/{total}\n")

    final_feedback = session.pop("final_feedback",None)
    return render_template("result.html", score=session["score"], total=total, final_feedback=final_feedback)

if __name__ == "__main__":
    app.run(debug=True)
        
