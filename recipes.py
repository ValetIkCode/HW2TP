class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value= float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным.")
        self._quantity= value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient({self.name!r}, {self.quantity!r}, {self.unit!r})"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return (self.name == other.name) and (self.unit == other.unit)
    
class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        self.ingredients = []

        if ingredients != None:
            for i in ingredients:
                self.add_ingredient(i)

    def add_ingredient(self, ingredient):
        for i in range(len(self.ingredients)):
            if self.ingredients[i] == ingredient:
                self.ingredients[i].quantity = self.ingredients[i].quantity + ingredient.quantity
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if (type(ratio) == int) or (type(ratio) == float):
            if ratio > 0:
                return True
        return False

    def scale(self, ratio):
        if Recipe.is_valid_ratio(ratio) == False:
            raise ValueError("Коэффициент должен быть положительным")
        new_recipe = Recipe(self.title)

        for ingredient in self.ingredients:
            name = ingredient.name
            quantity = ingredient.quantity * ratio
            unit = ingredient.unit

            new_ingredient = Ingredient(name, quantity, unit)
            new_recipe.add_ingredient(new_ingredient)

        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = self.title
        for ingredient in self.ingredients:
            result = result + "\n- " + str(ingredient)
        return result

class ShoppingList:
    def __init__(self):
        self.items = []

    def add_recipe(self, recipe, portions):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным.")
        new_recipe = recipe.scale(portions)
        for ingredient in new_recipe.ingredients:
            self.items.append((ingredient, recipe.title))

    def remove_recipe(self, title):
        result= []

        for item in self.items:
            if item[1]!=title:
                result.append(item)
        self.items = result

    def get_list(self):
        result = []

        for item in self.items:
            ingredient = item[0]
            found = False
            for current in result:
                if (current.name == ingredient.name) and (current.unit == ingredient.unit):
                    current.quantity+=ingredient.quantity
                    found = True
            if not found:
                result.append(Ingredient(ingredient.name, ingredient.quantity,ingredient.unit))
        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list.items = self.items + other.items
        return new_list