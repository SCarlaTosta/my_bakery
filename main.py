from models.ingredient import Ingredient
from models.recipe import    Recipe
flour = Ingredient("Un", 20, "kg")
salt = Ingredient("Tuz", 12, "kg")
milk = Ingredient("Süt", 28, "litre")



P =Recipe("poğaça")

P.add_ingredient(123,1)
P.add_ingredient(salt,0.020)


print(flour, salt, milk)