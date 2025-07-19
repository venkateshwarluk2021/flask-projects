# Recipe Manager (Flask App)

This is a simple **Recipe Manager web application** built with Python and Flask. It allows users to:

- Add new recipes
- Edit existing recipes
- Delete recipes
- List all recipes on the homepage
- Save and load recipes from a JSON file


---

## 🚀 Features

- Prevents duplicate recipe titles (case-insensitive and trimmed)
- Uses Bootstrap for a simple responsive layout
- Flash messages for user feedback (add/update/delete)
- Confirmation prompt before deleting
- Recipes are stored persistently in `recipes.json`

---

## ⚙️ How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/venkateshwarluk2021/flask-practice.git
   cd flask-practice/recipe_manager2

## Set up a virtual environment (optional

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

## Install Flask

pip install flask

## Run the app

python app.py

## Open in browser
Navigate to: http://127.0.0.1:5000

## 📝 Sample Usage
- Click "Add new Recipe" to add a recipe with title, ingredients, and steps.
- Edit or delete any existing recipe from the homepage.
- Recipes are saved in a recipes.json file automatically.
