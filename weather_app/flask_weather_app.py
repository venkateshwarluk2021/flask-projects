import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city").strip()
        if not city:
            error = "Please enter a city"

        else:
            params = {
                "key" : API_KEY,
                "q" : city,
                "aqi" : "no"
                }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city" : data["location"]["name"],
                    "temp_c" : data["current"]["temp_c"],
                    "desc" : data["current"]["condition"]["text"],
                    "humidity" : data["current"]["humidity"]
                    }
            else:
                error = "Could not fetch weather api. check city or API_KEY"

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
    
