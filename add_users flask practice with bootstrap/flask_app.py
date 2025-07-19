from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    message="Flask is awesome"
    return render_template("boot.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
