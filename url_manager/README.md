# 🔗 URL Manager - Flask Mini Project

This is a mini web application built using **Flask** to manage and display a list of useful URLs. It is part of my ongoing practice to master Flask, HTML templating, Bootstrap, and basic file handling in Python.

## 🚀 Features

- Add new URLs with titles and descriptions
- View a list of saved URLs
- Bootstrap layout for a clean and responsive UI
- Data is stored in a plain text file (`urls.txt`)

## 🛠 Tech Stack

- Python 3
- Flask
- HTML + Bootstrap 5
- Jinja2 Templates


## 💡 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/venkateshwarluk2021/flask-practice.git
   cd flask-practice/url_manager

## (Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

## Install dependencies

pip install flask


## Run the app

flask run

Open your browser and visit: http://127.0.0.1:5000

## Learning Highlights

- Flask route and template structure
- Working with form inputs in HTML
- Passing and rendering data in templates
- Reading from and writing to files
- Using Bootstrap for styling

## 🔐 Security Note

- The app uses a config.py file to store Flask's SECRET_KEY, which is excluded from version control using .gitignore.
-  In production, it's recommended to use environment variables or secret managers
