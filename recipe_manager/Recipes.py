class Recipe:
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"Recipe: {self.title}\n" \
               f"Ingredients: {','.join(self.ingredients)}\n" \
               f"Steps: \n"+"\n".join(f"- {step}" for step in self.steps)


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self,recipe):
        self.recipes.append(recipe)

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
            return True
        return False
