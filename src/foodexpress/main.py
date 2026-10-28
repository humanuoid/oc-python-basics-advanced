from foodexpress.entities.dish import Dish

products = [
    Dish("Pizza", 12.0, True),
    Dish("Tiramisu", 6.0, False)
]

for product in products:
    print(product.describe())
