import unittest
from recipe import Recipe
from recipe_manager import RecipeManager
import os

class TestRecipe(unittest.TestCase):

    def test_to_dict_and_from_dict(self):
        recipe = Recipe("Tea", ["Water","Tea Leaves"],["Boil water", "Add leaves"])
        d = recipe.to_dict()
        recipe2 = Recipe.from_dict(d)
        self.assertEqual(recipe.title, recipe2.title)
        self.assertEqual(recipe.ingredients, recipe2.ingredients)
        self.assertEqual(recipe.steps, recipe2.steps)

class TestRecipeManager(unittest.TestCase):

    def setUp(self):
        self.manager = RecipeManager()
        self.recipe = Recipe("Coffee", ["water","coffee powder"],["boil water", "add powder"])
        self.manager.add_recipe(self.recipe)

    def test_add_and_list(self):
        self.assertIn(self.recipe, self.manager.list_recipes())

    def test_find_recipe(self):
        result = self.manager.find_recipes_by_title("Coffee")
        self.assertEqual(result.title, "Coffee")

    def test_update_recipe(self):
        updated = Recipe("Coffee",["water", "instant coffee"],["mix and stir"])
        success = self.manager.update_recipe("Coffee", updated)
        self.assertTrue(success)
        self.assertEqual(self.manager.find_recipes_by_title("Coffee").ingredients[1], "instant coffee")

    def test_delete_recipe(self):
        success, msg = self.manager.delete_recipe("Coffee")
        self.assertTrue(success)
        self.assertEqual(msg, "Deleted successfully")
        self.assertIsNone(self.manager.find_recipes_by_title("Coffee"))

    def test_save_and_load(self):
        self.manager.filename = "test_recipes.json"
        self.manager.save_to_file()
        new_manager = RecipeManager("test_recipes.json")
        new_manager.load_from_file()
        self.assertEqual(len(new_manager.list_recipes()), 1)
        self.assertEqual(new_manager.list_recipes()[0].title,"Coffee")

    def tearDown(self):
        if os.path.exists("test_recipes.json"):
            os.remove("test_recipes.json")
        

if __name__ == "__main__":
    unittest.main()

