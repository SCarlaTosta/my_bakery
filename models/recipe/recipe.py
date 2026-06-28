from models.ingredient import Ingredient
class Recipe:
    def __init__(self,name):
        if not name.strip():
            raise ValueError("invalid name!")
        self.name = name

        self.ingredients = {}


    def add_ingredient(self,ingredient,amount):
        if  not isinstance(ingredient,Ingredient):

            raise TypeError("value must be ingredient object")



        if not  isinstance(amount,int):

            raise   TypeError("invalid amount")


        if amount <= 0:
            raise ValueError("amount can not be 0 or negative")

        self.ingredients[ingredient] = amount

    def remove_ingredient(self,ingredient):
        if not isinstance(ingredient,Ingredient):

            raise TypeError("value must be ingredient object")

