import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city):
    params = {
        "key" : api_key,
        "q" : city,
        "aqi" : "yes"
        }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]

        print(f"City: {city_name}")
        print(f"Temperature: {temp_c}")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}")
    else:
        print("Error . could not check weather report. check city or api key")


if __name__ == "__main__":
    print("============Weather Repost==========")
    city = input("Enter cuty name: \t").strip()
    get_weather(city)
    
