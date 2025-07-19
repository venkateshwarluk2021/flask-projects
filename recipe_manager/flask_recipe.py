from flask import Flask, render_template, request, redirect, url_for
from Recipes import Recipe, RecipeManager

app = Flask(__name__)
manager = RecipeManager()

@app.route("/")
def index():
    recipes = manager.list_recipes()
    return render_template('index.html', recipes=recipes)

@app.route("/add",methods=["GET","POST"])
def add_recipe():
    if request.method == "POST":
        title = request.form["title"]
        ingredients = request.form['ingredients'].split(',')
        steps = request.form['steps'].split('\n')
        recipe = Recipe(title, ingredients, steps)
        manager.add_recipe(recipe)
        return redirect(url_for("index"))
    return render_template("add.html")

if __name__ =="__main__":
    app.run(debug=True)
