from flask import Flask, render_template, request, redirect, url_for, flash
from recipe import Recipe
from recipe_manager import RecipeManager
from config import SECRET_KEY

app = Flask(__name__)
manager = RecipeManager()
manager.load_from_file()
app.secret_key = SECRET_KEY

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
        success = manager.add_recipe(recipe)
        if not success:
            flash("A recipe with this title already exists", "warning")
            return redirect(url_for('add_recipe'))
        else:
            flash("Recipe added successfully", "success")
            manager.save_to_file()
            return redirect(url_for('index'))
  
    return render_template("add.html")

@app.route("/edit/<title>", methods=["GET","POST"])
def edit_recipe(title):
    recipe = manager.find_recipes_by_title(title)
    if not recipe:
        return "Recipe not found", 404

    if request.method == "POST":
        new_title = request.form["title"]
        ingredients = request.form["ingredients"].split(",")
        steps = request.form["steps"].split("\n")

        existing = manager.find_recipes_by_title(new_title)
        if existing and new_title.lower() != title.lower():
            flash("Another recipe with this title already exists", "warning")
            return redirect(url_for('edit_recipe', title=title))

        
        updated_recipe = Recipe(title, ingredients, steps)
        manager.update_recipe(title, updated_recipe)
        flash("Recipe updated successfully","info")
        manager.save_to_file()
        return redirect(url_for("index"))
    return render_template("edit.html", recipe=recipe)


@app.route("/delete/<title>", methods=["POST"])
def delete_recipe(title):
    manager.delete_recipe(title)
    flash("Recipe deleted successfully","danger")
    manager.save_to_file()
    return redirect(url_for("index"))


if __name__ =="__main__":
    app.run(debug=True)
