# Feedback Flask App

A simple web application built with Flask, SQLite, and Bootstrap that allows users to submit feedback through a form. The feedback is stored in a database and can be viewed, deleted, or exported to CSV/JSON format.

## 🌟 Features

- Submit feedback with **name, email, message, and timestamp**
- View all submitted feedbacks in a styled Bootstrap table
- Flash message confirmation after feedback submission
- Export all feedbacks to:
  - CSV
  - JSON
- Toggle between **light/dark mode**
- Delete individual feedback entries from the UI

## 🛠 Tech Stack

- Python 3
- Flask
- SQLite
- Bootstrap 5
- HTML/CSS


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/venkateshwarluk2021/flask-practice.git
cd flask-practice/feedback_app

## Install dependencies (optional virtual env)

pip install flask

## pip install flask

python flask_feedback_app.py

Open your browser and go to http://127.0.0.1:5000

## Export Options

You can export all feedbacks with the buttons provided on the feedback list page:

- Download CSV
- Download JSON

