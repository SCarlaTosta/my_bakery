class Ingredient:
    units = ["kg", "gram", "litre", "adet"]
    def __init__(self,name,price,unit):

        if not name.strip():
            raise ValueError("NAME can not be empty")

        if  not isinstance(price,(int,float)):
            raise TypeError("price must be a number")


        if price < 0:
            raise ValueError("PRİCE can not be under zero")



        if not unit in Ingredient.units:
            raise ValueError("invalid unit")



        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self):
        return f"{self.name}   {self.price} TL/{self.unit}"


    def __repr__(self):
        return self.name




