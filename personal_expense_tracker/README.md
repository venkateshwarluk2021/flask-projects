# Personal Expense Tracker

A Flask-based web application to help users track their expenses. Users can add, view, and categorize expenses, and monitor spending over time.

---

## Table of Contents

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Future Improvements](#future-improvements)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Add new expenses with details like amount, date, category, description  
- View list of all expenses  
- Filter or view by category / date range  
- Edit or delete expense entries  
- Show summaries or totals (e.g. total spending per category or over a period)  
- Simple user-friendly interface via HTML templates  

---

## Technologies Used

- Python 3.x  
- Flask framework  
- Jinja2 templating  
- HTML / CSS (optionally JS) for frontend  
- (Optionally) SQLite or any lightweight database for storing expenses  
- ● Any third-party library you used (e.g. Flask-WTForms, Flask-SQLAlchemy)  

---

## Installation

1. **Clone the repository**

   - ```bash
   - git clone https://github.com/venkateshwarluk2021/flask-practice.git
   - cd flask-practice/personal_expense_tracker
2. **Set up a Python virtual environment**
- python3 -m venv venv
- source venv/bin/activate    # On Linux / macOS
# or on Windows
- venv\Scripts\activate

3. **Install dependencies**
- If there is a requirements.txt file: pip install -r requirements.txt
- Otherwise install manually: pip install flask
- # plus any ORM, form libraries, etc.


4. **Database setup**
- If using a database (e.g. SQLite), make sure to initialize it:flask db init       # if using flask-migrate or similar
-- flask db migrate
-- flask db upgrade

# Configuration 
-- Environment variables:

-- FLASK_ENV — set to development for debug mode

-- Any secret key or configuration settings (if applicable)

-- Database URI or path

-- If using .env file, store sensitive info there (and do not commit it).

# Usage
- Activate the virtual environment (venv).
- Run the Flask app: flask run
- or if your main file is e.g. app.py: python app.py
- Access the app in your browser, typically at http://127.0.0.1:5000
- From the UI:
-- Add new expenses

-- View the list of all expenses

-- Filter or search by category or date

-- Edit or delete entries
 
