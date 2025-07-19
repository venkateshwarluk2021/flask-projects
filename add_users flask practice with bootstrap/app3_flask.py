from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    return f"Received: {name} ({email})"

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

@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html" , username=username)

if __name__ == "__main__":
    app.run(debug=True)
