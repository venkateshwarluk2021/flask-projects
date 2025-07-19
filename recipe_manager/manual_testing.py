from recipe_manager import RecipeManager
from recipe import Recipe

if __name__ == "__main__":
    manager= RecipeManager()

    r1 = Recipe("Pasta", ["pasta", "sauce"],["Boil pasta","Add sauce"])
    r2 = Recipe("Salad", ["lettuce", "tomato"],["Chop lettuce","Add tomato"])

    manager.add_recipe(r1)
    manager.add_recipe(r2)

    for recipe in manager.list_recipes():
        print(recipe)
        print("-"*30)


    found = manager.find_recipes_by_title("Pasta")
    if found:
        print("Recipe found")
        print(found)

    deleted = manager.delete_recipe("Pasta")
    print("Deleted: ", deleted)
