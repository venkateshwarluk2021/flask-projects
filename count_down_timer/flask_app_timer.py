from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    countdown_time = None
    if request.method == "POST":
        try:
            countdown_time = int(request.form["seconds"])
        except ValueError:
            countdown_time = None
    return render_template("index.html", countdown_time=countdown_time)

if __name__ == "__main__":
    app.run(debug=True)
