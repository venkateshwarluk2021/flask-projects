import pytest
import os
from recipe import Recipe
from recipe_manager import RecipeManager

TEST_FILE = "test_recipes.json"

@pytest.fixture
def manager():
    # Setup: create a new RecipeManager with a test file
    mgr = RecipeManager(filename=TEST_FILE)
    mgr.recipes = [] # start with a clean state
    yield mgr
    # Teardown: remove test file after test run
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_recipe_success(manager):
    recipe = Recipe("Test Tea",["Water","Tea Leaves"],["Boil water","Add Tea Leaves"])
    result = manager.add_recipe(recipe)
    assert result is True
    assert len(manager.recipes) == 1

def test_add_duplicate_recipe(manager):
    recipe1 = Recipe("Tea",["Water"],["Boil water"])
    recipe2 = Recipe("tea",["Water","Milk"],["Different method"])
    manager.add_recipe(recipe1)
    result = manager.add_recipe(recipe2)
    assert result is False
    assert len(manager.recipes) == 1

def test_find_recipe(manager):
    recipe = Recipe("Coffee",["Water","Coffee powder"],["Boil water","Add powder"])
    manager.add_recipe(recipe)
    found = manager.find_recipes_by_title("coffee")
    assert found is not None
    assert found.title == "Coffee"

def test_delete_recipe_success(manager):
    recipe = Recipe("Soup",["Water","vegetables"],["Boil","serve"])
    manager.add_recipe(recipe)
    deleted, msg = manager.delete_recipe("soup")
    assert deleted is True
    assert msg == "Deleted successfully"
    assert len(manager.recipes) == 0

def test_delete_recipe_not_found(manager):
    deleted, msg = manager.delete_recipe("NonExistent")
    assert deleted is False
    assert msg == "Recipe not found"

def test_update_recipe_success(manager):
    old = Recipe("Maggi",["Noodles"],["Boil water","Add noodles"])
    updated = Recipe("Maggi",["Noodles","masala"],["cook properly"])
    manager.add_recipe(old)
    result = manager.update_recipe("Maggi", updated)
    assert result is True
    assert manager.recipes[0].ingredients == ["Noodles","masala"]

def test_update_recipe_not_found(manager):
    updated = Recipe("upma",["Ravva"],["Cook it"])
    result = manager.update_recipe("NonExistent", updated)
    assert result is False

def test_load_and_save(manager):
    recipe = Recipe("Poha",["Poha","Onion"],["Rinse","Cook"])
    manager.add_recipe(recipe)
    manager.save_to_file()

    # Create new manager and load from saved file
    new_manager = RecipeManager(filename=TEST_FILE)
    new_manager.load_from_file()
    assert len(new_manager.recipes) == 1
    assert new_manager.recipes[0].title == "Poha"
    
