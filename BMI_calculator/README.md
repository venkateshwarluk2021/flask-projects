# BMI Calculator

A simple Flask web application that calculates the Body Mass Index (BMI) for users based on their height and weight, and shows interpretation based on the result.

---

## Table of Contents

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  


---

## Features

- Input weight and height via a form.  
- Calculates BMI using the formula:  
- BMI = weight (kg) / (height (m))²
- Displays BMI value and a category (e.g. Underweight, Normal, Overweight, Obese) based on standard thresholds.  
- Basic error handling (invalid inputs, missing fields, non-numeric input).  
- Clean, minimal front-end with form and result display (via Flask templates).

---

## Technologies Used

- Python  
- Flask  
- HTML / CSS  
- (Optional: if used) Bootstrap or other CSS framework  
- (Optional: if used) WTForms or similar for form validation  

---

## Installation

1. **Clone the repository**  
 - ```bash
 - git clone https://github.com/venkateshwarluk2021/flask-practice.git
 - cd flask-practice/BMI_calculator

## Create and activate a virtual environment
- python3 -m venv venv
- source venv/bin/activate     # on Linux / macOS
 # or
- venv\Scripts\activate        # on Windows

## Install dependencies
- If there is a requirements.txt pip install -r requirements.txt
- Otherwise install needed packages manually
- pip install flask
- ( plus any others if used)

## Configuration
- If you have any configuration (e.g. secret keys, template settings), set them as environ-variables or config files.

- If using debug mode, set FLASK_ENV=development (or similar)

## Usage
- Ensure your virtual environment is activated.

- Run the Flask application. For example
- flask run or python app.py

- Open your browser and go to: http://127.0.0.1:5000
- On the home page, enter your weight (in kg) and height (in meters or cm, depending) and submit.

View your calculated BMI and the category interpretation


## Docker Support

### Build Image
docker build -t bmi-calculator .

### Run Container
docker run -p 5000:5000 bmi-calculator

### Pull from Docker Hub
docker pull kvenkat2026/bmi-calculator

docker run -p 5000:5000 kvenkat2026/bmi-calculator

