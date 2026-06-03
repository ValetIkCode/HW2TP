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
    def is_valid(ratio):
        if (type(ratio) == int) or (type(ratio) == float):
            if ratio > 0:
                return True
        return False

    def scale(self, ratio):
        if Recipe.is_valid(ratio) == False:
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