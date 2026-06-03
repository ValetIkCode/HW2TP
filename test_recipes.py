import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient():
    i = Ingredient("Мука", 67, "г")
    assert i.name=="Мука"
    assert i.quantity == 67.0
    assert i.unit=="г"

def test_bad_ingredient():
    with pytest.raises(ValueError):
        Ingredient("Сыр", 0, "г")

def test_recipe():
    r = Recipe("Студенческая пицца")
    r.add_ingredient(Ingredient("Лаваш", 1, "шт"))
    r.add_ingredient(Ingredient("Сыр", 228, "г"))
    r.add_ingredient(Ingredient("Сыр", 50, "г"))

    assert len(r)==2
    assert r.ingredients[1].quantity == 278.0

def test_scale_recipe():
    r = Recipe("Пельмени со сметаной")
    r.add_ingredient(Ingredient("Пельмени", 1337, "г"))
    r.add_ingredient(Ingredient("Сметана", 100, "г"))

    r2 = r.scale(2)
    assert r2.ingredients[0].quantity == 2674.0
    assert r2.ingredients[1].quantity == 200.0

def test_bad_scale():
    r = Recipe("Доширак")

    with pytest.raises(ValueError):
        r.scale(0)

def test_shopping_list():
    r1 = Recipe("Доширак")
    r1.add_ingredient(Ingredient("Лапша", 1, "пачка"))
    r2 = Recipe("Ночной дошик")
    r2.add_ingredient(Ingredient("Лапша", 2, "пачка"))

    sp = ShoppingList()
    sp.add_recipe(r1, 1)
    sp.add_recipe(r2, 1)
    
    result = sp.get_list()

    assert len(result) == 1
    assert result[0].quantity == 3.0

def test_remove_recipe():
    r = Recipe("Пельмени со сметаной")
    r.add_ingredient(Ingredient("Пельмени", 500, "г"))
    
    sp = ShoppingList()
    sp.add_recipe(r, 1)
    sp.remove_recipe("Пельмени со сметаной")

    assert sp.get_list()==[]

def test_diet_recipe():
    r = DietaryRecipe("Овощной салат", "веган")
    r.add_ingredient(Ingredient("Огурец", 1, "шт"))
    r.add_ingredient(Ingredient("Помидор", 1, "шт"))

    assert r.diet_type == "веган"
    assert str(r) == "[веган] Овощной салат\n- Огурец: 1.0 шт\n- Помидор: 1.0 шт"