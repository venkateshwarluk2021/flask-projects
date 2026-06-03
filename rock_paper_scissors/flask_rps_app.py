from flask import Flask, request, jsonify, render_template
from game.game_engine import Game

app = Flask(__name__)
game = Game()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play-ui", methods=["POST"])
def play_ui():
    choice = request.form.get("choice")

    try:
        result = game.play_round(choice)
        return render_template("index.html", result=result)
    except ValueError as e:
        return render_template("index.html", error=str(e))


@app.route("/play", methods=["POST"])
def play_api():
    data = request.get_json()

    if not data or "choice" not in data:
        return jsonify({"error": "Please provide 'choice'"}), 400

    try:
        result = game.play_round(data["choice"].lower())
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
