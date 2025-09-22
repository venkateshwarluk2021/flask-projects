# Countdown Timer

A Flask web application that lets users set a countdown timer and displays the remaining time until completion.

---

## Table of Contents

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  


---

## Features

- Set a countdown timer (hours/minutes/seconds) via a web form.  
- Display the live remaining time updating in real time.  
- On timer expiry, show a message or indication that the countdown is complete.  
- Basic validation to ensure timer values are non-negative / valid.  

---

## Technologies Used

- Python 3.x  
- Flask  
- HTML / CSS / JavaScript (for real-time front-end countdown display)  
- (Optional) Flask templates (Jinja2)  
- (Optional) Any libraries used for time or client-side update  

---

## Installation

1. **Clone the repository**

   - ```bash
   - git clone https://github.com/venkateshwarluk2021/flask-practice.git
   - cd flask-practice/count_down_timer
2. **Set up a virtual environment**
- python3 -m venv venv
- source venv/bin/activate   # Linux/macOS
# or on Windows
- venv\Scripts\activate

3. **Install dependencies**
- If there is a requirements.txt: pip install -r requirements.txt
- Otherwise manually: pip install flask
# plus any JavaScript/CSS assets you used

## Usage
- Ensure your virtual environment is activated.
- Run the Flask application: flask run
- or python app.py   # or whatever your main file is
- Open your browser and go to: http://127.0.0.1:5000
- Use the form to set the time duration you want for the countdown.
- Once started, you will see the timer count down in real time until it reaches zero.
- After the timer ends, an indication or message will show that the countdown is complete.
