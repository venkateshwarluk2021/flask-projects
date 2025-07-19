import json
from recipe import Recipe

class RecipeManager:
    def __init__(self, filename="recipes.json"):
        self.recipes = []
        self.filename = filename


    def add_recipe(self,recipe):
        if self.find_recipes_by_title(recipe.title):
            return False
        self.recipes.append(recipe)
        return True

    def list_recipes(self):
        return self.recipes

    def find_recipes_by_title(self, title):
        for recipe in self.recipes:
            if recipe.title.lower() == title.lower():
                return recipe
        return None

    def delete_recipe(self, title):
        recipe = self.find_recipes_by_title(title)
        if recipe:
            self.recipes.remove(recipe)
            return True, "Deleted successfully"
        return False, "Recipe not found"

    def update_recipe(self, original_title, new_recipe):
        for i, j in enumerate(self.recipes):
            if j.title.lower() == original_title.lower():
                self.recipes[i] = new_recipe
                return True
        return False

    def save_to_file(self):
        with open(self.filename , "w") as fp:
            json.dump([r.to_dict() for r in self.recipes], fp, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as fp:
                data = json.load(fp)
                self.recipes = [Recipe.from_dict(d) for d in data]
        except FileNotFoundError:
            self.recipes = []
    
        
