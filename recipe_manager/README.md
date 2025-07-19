# 🥘 Recipe Manager - Flask Mini Project

This is a simple **Recipe Manager** web application built using **Flask** and **HTML (Bootstrap)**. The project is part of my personal learning to understand how to build a complete web app using Python, Flask, forms, and basic file storage.

## 🚀 Features

- View all recipes
- Add a new recipe (Title, Ingredients, Steps)
- Edit an existing recipe
- Delete a recipe (with confirmation)
- Flash messages for actions (like “Recipe added”, “Recipe deleted”)
- Stores recipe data in a text file (`recipes.txt`)

## 🛠 Tech Stack

- Python 3
- Flask
- HTML + Jinja2 Templates
- Bootstrap 5


## 💡 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/venkateshwarluk2021/flask-practice.git
   cd flask-practice/recipe_manager

## (Optional) Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies

pip install flask

## Run the Flask app:

flask run

Open your browser and go to: http://127.0.0.1:5000

## Learning Goals

Build a full CRUD app using Flask
Use object-oriented Python for logic (Recipe and RecipeManager) 
Connect HTML forms to Flask routes 
Handle flash messages and confirmation prompts 
Store and retrieve data from a plain text file
