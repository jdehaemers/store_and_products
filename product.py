class Product:
    all_products = []
    
    def __init__(self, name, price, category):
        self.name     = name
        self.price    = price
        self.category = category
        self.id       = len(type(self).all_products)
        type(self).all_products.append(self)

    def update_price(self, percent_change, is_increased):
        sign = 1
        if not is_increased:
            sign *= -1
        self.price *= 1 + percent_change / 100 * sign
    
    def print_info(self):
        print(f'{self.name}: ${round(float(self.price),2)} - {self.category}')

