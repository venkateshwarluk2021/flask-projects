import os
import requests
from tkinter import Tk, Label, Entry, Button, StringVar
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather():
    city = city_var.get().strip()
    if not city:
        result_var.set("Please enter a city")
        return
    params = {
        "key" : API_KEY,
        "q" : city,
        "aqi" : "no"
        }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            city_name = data["location"]["name"]
            temp_c = data["current"]["temp_c"]
            desc = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]

            result_text = (
                f"City: {city_name}\n"
                f"Temperature: {temp_c} °C\n"
                f"Weather: {desc}\n"
                f"Humidity: {humidity}%"
                )

            result_var.set(result_text)
        else:
            result_var.set("Could not fetch weather")
    except Exception as e:
        result_var.set(f"Error: {str(e)}")



root = Tk()
root.title("Weather Report App")
root.geometry("350x250")

Label(root, text="Enter city: ", font=("Arial", 12)).pack(pady=5)
city_var = StringVar()
Entry(root, textvariable=city_var, font=("Arial", 12)).pack(pady=5)

Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="lightblue").pack(pady=10)
result_var = StringVar()
Label(root, textvariable=result_var, font=("Arial", 12), justify="left", wraplength=300).pack(pady=10)

root.mainloop()
            
