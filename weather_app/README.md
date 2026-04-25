# Weather App

A simple Flask application to fetch and display weather information for a given location.

---

## Table of Contents

1. [Features](#features)  
2. [Technologies Used](#technologies-used)  
3. [Installation](#installation)  



---

## Features

- Enter a city (or other location identifier) to get current weather information  
- Display key weather details: temperature, humidity, wind, etc.  
- Nicely styled frontend using HTML/CSS (template rendering with Flask)  
- Error handling for invalid locations or API failures  

---

## Technologies Used

- **Python**  
- **Flask** — Web framework  
- HTTP requests via `requests` (or whichever HTTP library)  
- HTML / CSS / (optionally JavaScript) for frontend  
- External weather API (e.g. OpenWeatherMap or similar)  

---

## Installation

1. **Clone the repository**

  -  ```bash
   - git clone https://github.com/venkateshwarluk2021/flask-practice.git
   - cd flask-practice/weather_app

2. Create & activate a virtual environment
  -  python3 -m venv venv
  - source venv/bin/activate   # on Linux / macOS
  # or
 -  venv\Scripts\activate      # on Windows

3.  Install dependencies
   - pip install -r requirements.txt
   - If there is no requirements.txt, manually install:
   - pip install flask requests
   # …and any other packages used

4.  Configuration
    - You may need to set up configuration items such as:
      
     -  API key for the weather service
      
     -  Host/port (if not using default)
      
      - Debug mode

5.  Example using environment variables:
    - export WEATHER_API_KEY="your_api_key_here"
    - export FLASK_ENV=development

  - or use a .env file + python-dotenv if included.
 
6.  Usage
   - Activate environment (if not already).
    - Run the Flask app: flask run
   -  Or (if app.py is the main entry): python app.py
   -  Open browser and go to http://127.0.0.1:5000 (or the appropriate host/port)
   -  Input a city/location, submit, and view weather details.

