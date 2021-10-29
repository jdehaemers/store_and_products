from product import *

class Store:
    def __init__(self, name):
        self.name     = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        x = Product.all_products[id]
        x.print_info()
        self.products.remove(x)
    
    def inflation(self, percent_increase):
        for p in self.products:
            p.update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for p in self.products:
            if p.category == category:
                p.update_price(percent_discount, False)

