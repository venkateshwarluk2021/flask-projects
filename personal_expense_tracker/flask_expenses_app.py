from flask import Flask, render_template, request, redirect, url_for, flash
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mysecretkey"

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="") as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as fp:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


@app.route("/")
def index():
    expenses = load_expenses()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    category = request.form["category"]
    amount = request.form["amount"]
    note = request.form["note"]
    try:
        amount = float(amount)
        if not category or amount <= 0:
            raise ValueError
        date = datetime.now().strftime("%Y-%m-%d")
        expenses = load_expenses()
        expenses.append({"date":date, "category":category,"amount":amount,"note":note})
        save_expenses(expenses)
        flash("Expense added successfully", "success")
    except:
        flash("Invalid input", "danger")
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        save_expenses(expenses)
        flash(f"Deleted: {deleted['category']} - {deleted['amount']}", "info")
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_expense(index):
    expenses = load_expenses()
    if request.method == "POST":
        try:
            expenses[index]["category"] = request.form["category"]
            expenses[index]["amount"] = float(request.form["amount"])
            expenses[index]["note"] = request.form["note"]
            save_expenses(expenses)
            flash("Expense updated", "success")
            return redirect(url_for("index"))
        except:
            flash("invalid data","danger")
    return render_template("edit.html", expense=expenses[index], index=index)

@app.route("/search", methods=["POST"])
def search_expense():
    keyword = request.form["keyword"].lower()
    expenses = load_expenses()
    results = [exp for exp in expenses if keyword in exp["category"].lower() or
               keyword in exp["note"].lower() or
               keyword in exp["date"]]
    return render_template("index.html", expenses=results, keyword=keyword)


@app.route("/summary")
def summary():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0)+exp["amount"]
    return render_template ("index.html", expenses=expenses, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
