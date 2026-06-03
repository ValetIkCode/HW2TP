# Recipe Manager

## Автор
Тимошенко Валерий, ББИ2507

## Описание проекта

Проект для управления рецептами, ингредиентами и списками покупок.

В проекте реализованы классы
* `Ingredient` 
* `Recipe` 
* `ShoppingList` 
* `DietaryRecipe` 

## Установка

Устанавливаем зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска тестов команда:

```bash
python -m pytest
```

## Файлы
* `recipes.py` - основные классы проекта
* `test_recipes.py` - тесты для проверки работы классов
* `requirements.txt` - список зависимостей
* `.gitignore` - исключения для Git

## Использование

Пример создания рецепта:

```python
from recipes import Ingredient, Recipe

recipe = Recipe("Студенческая пицца")
recipe.add_ingredient(Ingredient("Лаваш", 1, "шт"))
recipe.add_ingredient(Ingredient("Сыр", 100, "г"))
recipe.add_ingredient(Ingredient("Сосиски", 200, "г"))
print(recipe)
```
