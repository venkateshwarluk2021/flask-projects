from flask import Flask, request, jsonify
from game.game_engine import Game

app = Flask(__name__)

#create game instance
game = Game()


@app.route("/")
def home():
    return jsonify({"message": "ROck Paper Scissors API is running"})

@app.route("/play",methods=["POST"])
def play():
    data = request.get_json()

    if not data or "choice" not in data:
        return jsonify({"error":"Please provide 'choice'"}), 400

    try:
        result = game.play_round(data["choice"].lower())
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
