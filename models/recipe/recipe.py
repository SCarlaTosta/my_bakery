from models.ingredient import Ingredient
class Recipe:
    def __init__(self,name):
        if not name.strip():
            raise ValueError("invalid name!")
        self.name = name

        self.ingredients = {}


    def __str__(self):
        return f"{self.name}"


    def add_ingredient(self,ingredient,amount):
        if  not isinstance(ingredient,Ingredient):

            raise TypeError("value must be ingredient object")



        if not  isinstance(amount,(int,float)):

            raise   TypeError("invalid amount")


        if amount <= 0:
            raise ValueError("amount can not be 0 or negative")

        self.ingredients[ingredient] = amount




    def remove_ingredient(self,ingredient):
        if not isinstance(ingredient,Ingredient):

            raise TypeError("value must be ingredient object")

        del self.ingredients[ingredient]


    def total_price(self):
        total = 0
        for ingredients,amount in self.ingredients.items():
            total += ingredients.price * amount
        return total


    def ingredient_count(self):
        return len(self.ingredients)



    def has_ingredient(self,ingredient):
        if not isinstance(ingredient,Ingredient):

            raise TypeError("value must be ingredient object")
        if  ingredient  not  in self.ingredients:
            return False

        return True



