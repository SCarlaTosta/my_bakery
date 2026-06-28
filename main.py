from models.ingredient import Ingredient
from models.recipe import    Recipe
flour = Ingredient("Un", 20, "kg")
salt = Ingredient("Tuz", 12, "kg")
milk = Ingredient("Süt", 28, "litre")



P =Recipe("poğaça")

P.add_ingredient(flour,1)
P.add_ingredient(salt,0.020)
print(P.ingredients)
print(P.total_price())


print(flour, salt, milk)