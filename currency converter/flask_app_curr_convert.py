# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.frankfurter.app/latest"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    currencies = ["USD", "EUR", "INR", "GBP", "JPY"]

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_curr = request.form["from_curr"]
            to_curr = request.form["to_curr"]

            if from_curr == to_curr:
                result = f"⚠️ Source and target currencies must be different."
            else:
                response = requests.get(f"{API_URL}?amount={amount}&from={from_curr}&to={to_curr}")
                data = response.json()
                if "rates" in data and to_curr in data["rates"]:
                    converted = data["rates"][to_curr]
                    result = f"✅ {amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
                else:
                    result = "❌ Conversion failed."
        except ValueError:
            result = "❌ Invalid amount entered."
        except Exception as e:
            result = f"❌ Error: {e}"

    return render_template("index.html", currencies=currencies, result=result)

if __name__ == "__main__":
    app.run(debug=True)
