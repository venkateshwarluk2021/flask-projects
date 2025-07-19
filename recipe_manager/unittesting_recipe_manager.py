import unittest
from Recipes import Recipe, RecipeManager


class TestRecipeManager(unittest.TestCase):

    def setUp(self):
        self.manager = RecipeManager()
        self.recipe = Recipe("Pasta",["pasta","sauce"],["Boil pasta","Add sauce"])
        self.manager.add_recipe(self.recipe)

    def test_add_recipe(self):
        self.assertIn(self.recipe, self.manager.recipes)

    def test_list_recipes(self):
        recipes = self.manager.list_recipes()
        self.assertEqual(len(recipes),1)
        self.assertEqual(recipes[0].title,"Pasta")

    def test_find_recipes_by_title(self):
        found = self.manager.find_recipes_by_title("pasta")
        self.assertIsNotNone(found)
        self.assertEqual(found.title,"Pasta")

    def test_delete_recipe(self):
        result = self.manager.delete_recipe("Pasta")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.recipes),0)

    def test_delete_nonexistent_recipe(self):
        result = self.manager.delete_recipe("Burger")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
