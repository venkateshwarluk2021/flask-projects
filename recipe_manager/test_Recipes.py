import pytest
from Recipes import Recipe, RecipeManager

@pytest.fixture
def sample_manager():
    manager = RecipeManager()
    recipe = Recipe("Pasta",["pasta","sauce"],["Boil pasta","Add sauce"])
    manager.add_recipe(recipe)
    return manager

def test_add_recipe(sample_manager):
    assert len(sample_manager.recipes) == 1
    assert sample_manager.recipes[0].title == "Pasta"

def test_list_recipes(sample_manager):
    recipes = sample_manager.list_recipes()
    assert isinstance(recipes, list)
    assert len(recipes) == 1

def test_find_recipes_by_title(sample_manager):
    found = sample_manager.find_recipes_by_title("Pasta")
    assert found is not None
    assert found.title =="Pasta"

def test_delete_recipe(sample_manager):
    result = sample_manager.delete_recipe("Pasta")
    assert result is True
    assert len(sample_manager.recipes) == 0

def test_delete_nonexistent_recipes(sample_manager):
    result = sample_manager.delete_recipe("Burger")
    assert result is False
    
