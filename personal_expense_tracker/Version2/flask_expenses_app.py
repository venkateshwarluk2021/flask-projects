from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3
from db import init_db, get_connection

app = Flask(__name__)
app.secret_key = "supersecret"

init_db()

def load_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [{"id":r[0],"date":r[1], "category":r[2], "amount":r[3], "note":r[4]} for r in rows]

def add_expense(category, amount, note):
    conn = get_connection()
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?,?,?,?)",
                   (date, category, amount, note))
    conn.commit()
    conn.close()


def delete_expense(exp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE fROM expenses where id=?",(exp_id,))
    conn.commit()
    conn.close()

def update_expense(exp_id, category, amount, note):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE expenses SET category=?, amount=?, note=? WHERE id=?",
                   (category, amount, note, exp_id))
    conn.commit()
    conn.close()

def search_expenses(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM expenses WHERE
                    category LIKE ? OR note LIKE ? OR date LIKE?""",
                   (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    conn.close()
    return [{"id":r[0],"date":r[1],"category":r[2], "amount":r[3], "note":r[4]} for r in rows]

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    return {r[0]:r[1] for r in rows}


@app.route("/")
def index():
    expenses = load_expenses()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_route():
    try:
        category = request.form["category"]
        amount = float(request.form["amount"])
        note = request.form["note"]
        add_expense(category, amount, note)
        flash("Expense added successfully", "success")
    except:
        flash("Invalid input", "danger")
    return redirect(url_for("index"))

@app.route("/delete/<int:exp_id>")
def delete_route(exp_id):
    delete_expense(exp_id)
    flash("Expense delete", "info")
    return redirect(url_for("index"))

@app.route("/edit/<int:exp_id>", methods=["GET", "POST"])
def edit_route(exp_id):
    if request.method == "POST":
        try:
            category = request.form["category"]
            amount = float(request.form["amount"])
            note = request.form["note"]
            update_expense(exp_id, category ,amount, note)
            flash("expense updated", "success")
            return redirect(url_for("index"))
        except:
            flash("Invalid data", "danger")

    expenses = load_expenses()
    exp = next((e for e in expenses if e["id"] == exp_id), None)
    if not exp:
        flash("exp not found", "danger")
        return redirect(url_for("index"))
    return render_template("edit.html", expense=exp)

@app.route("/search", methods=["POST"])
def search_route():
    keyword = request.form["keyword"]
    results = search_expenses(keyword)
    return render_template("index.html", expenses=results)

@app.route("/summary")
def summary_route():
    expenses = load_expenses()
    summary = get_summary()
    return render_template("index.html", expenses=expenses, summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
