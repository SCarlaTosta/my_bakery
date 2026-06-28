class Inventory:
    def __init__(self):
        self.product = {}


    def add_stock(self,item,amount):
        self.product[item.name] = item
        self.product[item.amount] = amount

