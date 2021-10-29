from product import *
from store import *

store = Store('Walmart')
apple    = Product('apple', 1.5, 'food')
banana   = Product('banana', 1, 'food')
computer = Product('computer', 100, 'tech')
discman  = Product('discman', 10, 'tech')
eggs     = Product('eggs', 4, 'food')
products = [apple, banana, computer, discman, eggs]

for p in products:
    store.add_product(p)

store.sell_product(0)
store.inflation(10)
store.set_clearance('tech', 40)

for p in store.products:
    p.print_info()

for p in store.products:
    print(p.id)

