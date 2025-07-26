from flask import Flask, render_template, request, redirect, flash, Response
import feedback_service
from feedback import Feedback
from config import SECRET_KEY
import csv
import json

app = Flask(__name__)
app.secret_key = SECRET_KEY

feedback_service.create_table()

@app.route("/")
def index():
    return render_template("feedback_form.html")

@app.route("/submit", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    feedback = Feedback(name, email, message)
    feedback_service.save_feedback(feedback)
    flash("Thank you for your feedabck")
    return redirect("/")

@app.route("/feedbacks")
def view_feedbacks():
    all_feedback = feedback_service.get_all_feedback()
    return render_template("view_feedbacks.html", feedbacks=all_feedback)


@app.route("/export/csv")
def export_csv():
    feedbacks = feedback_service.get_all_feedback()

    def generate():
        yield "ID, name, email, message, timestamp \n"
        for fb in feedbacks:
            line = f"{fb['ID']}, {fb['name']},{fb['email']}, {fb['message']}, {fb['timestamp']}\n"
            yield line

    return Response(generate(), mimetype="text/csv",
                    headers = {"Content-Disposition": "attachment; filename=feedbacks.csv"})


@app.route("/export/json")
def export_json():
    feedbacks = feedback_service.get_all_feedback()
    data = [dict(row) for row in feedbacks]
    return Response(
        json.dumps(data, indent=4),
        mimetype='application/json',
        headers={"Content-Disposition": "attachment; filename=feedbacks.json"}
        )

@app.route("/delete/<int:feedback_id>", methods=["POST"])
def delete_feedback(feedback_id):
    feedback_service.delete_feedback(feedback_id)
    flash(f"FEEDBACK ID {feedback_id} deleted")
    return redirect("/feedbacks")


if __name__ == "__main__":
    app.run(debug=True)
