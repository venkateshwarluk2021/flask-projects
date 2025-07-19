from flask import Flask, render_template

app = Flask(__name__)

@app.route("/table")
def table():
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
    ]
    return render_template("table.html", users=users)


@app.route("/cards")
def cards():
     users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
        ]
     return render_template("cards.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
