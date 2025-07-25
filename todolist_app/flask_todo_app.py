from flask import Flask, render_template, redirect, request, url_for, flash
from task_service import add_task, get_all_tasks, get_task_by_id, update_task, delete_task
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    tasks = get_all_tasks()
    return render_template('home.html', tasks=tasks)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        completed = "completed" in request.form
        add_task(title, description, deadline, completed)
        flash("Task added successfully")
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route("/edit/<int:task_id>", methods=["GET","POST"])
def edit(task_id):
    task = get_task_by_id(task_id)
    if request.method == "POST":
        title= request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        completed = "completed" in request.form
        update_task(task_id, title, description, deadline, completed)
        flash("Task updated")
        return redirect(url_for("index"))
    return render_template("edit_task.html", task=task)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    flash("Deleted task")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
