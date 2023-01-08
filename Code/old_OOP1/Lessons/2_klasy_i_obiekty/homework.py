
class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == '__main__':

    apple_1 = Apple()
    apple_2 = Apple()
    potato_1 = Potato()
    potato_2 = Potato()
    order_1 = Order()

    print('type (apple_1):', type(apple_1))
    print('type (apple_2):', type(apple_2))
    print('type (potato_1):', type(potato_1))
    print('type (potato_2):', type(potato_2))

order_1 = [apple_1, apple_2, potato_1]
order_2 = [Order(), Order(), Order()]

products = {
    'Ziemniak': Product(),
    "Jabłko": Product(),
    'Marchew': Product(),
    'Ananas': Product()
}
print(products)
print(order_1)
print(order_2)
