# Flask Quiz App 🧠✨

This is a simple Flask-based Quiz Web Application that presents multiple-choice questions to the user, tracks their progress and score, and displays the final result. The app uses Python OOP concepts and Flask templates, styled with Bootstrap.

## 🌟 Features

- Multiple choice questions loaded from Python file (`quiz_data.py`)
- Clean UI using Bootstrap
- Feedback after each question
- Score tracking
- Progress bar to visualize quiz progress
- Result page with final score
- Option to restart the quiz
- Home button on every page

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5, CSS3
- Bootstrap 5
- Jinja2 templating

## 🚀 Getting Started

### Prerequisites

Ensure Python is installed:

```bash
python --version

## Install Flask

pip install flask

##  Clone the Repository

git clone https://github.com/venkateshwarluk2021/flask-practice.git
cd flask-practice/Quizz_app


## Run the App

python app.py

## Visit http://127.0.0.1:5000 in your browser.

## Project Structure

Quizz_app/
├── app.py               # Main Flask app
├── config.py            # Secret key config
├── quiz_data.py         # Quiz question data
├── templates/
│   ├── base.html        # Common layout
│   ├── home.html        # Start page
│   ├── question.html    # Question and options
│   └── result.html      # Final score display
└── static/
    └── style.css        # Custom styling (if used)


