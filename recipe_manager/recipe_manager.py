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
    
        
