# Zadanie nr 1
#
# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
#
#     Product: nazwa, nazwa kategorii, cena jednostkowa
#     Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta),
#     łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
#     Apple: nazwa gatunku, rozmiar, cena za kg
#     Potato: nazwa gatunku, rozmiar, cena za kg
#
# Utwórz kilka obiektów każdej klasy.

# Zadanie nr 2
#
# Napisz funkcję wypisującą produkt i zamówienie.
# Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.

# Zadanie nr 3
#
# Napisz funkcję generującą zamówienie z
# losową listą produktów na przykład: Produkt-1, Produkt-2 itd.
import random


class Product:

    def __init__(self, name, category_name, price_per_unit):
        self.name = name
        self.category_name = category_name
        self.price_per_unit = price_per_unit


class Order:

    def __init__(self, first_name, last_name, product_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            product_list = []
        self.product_list = product_list

        total_price = 0
        for product in product_list:
            total_price += product.price_per_unit
        self.total_price = total_price


class Apple:

    def __init__(self, species, size, price_per_unit):
        self.species = species
        self.size = size
        self.price_per_unit = price_per_unit


class Potato:

    def __init__(self, species, size, price_per_unit):
        self.species = species
        self.size = size
        self.price_per_unit = price_per_unit


def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        name = f'Produkt-{product_number}'
        category_name = 'Inne'
        price_per_unit = random.randint(1, 20)
        product = Product(name, category_name, price_per_unit)
        products.append(product)

    order = Order(first_name='Janek', last_name="Franek", product_list=products)
    return order


def print_order(order):
    print('=' * 20)
    print(f'Zamówienie złożone przez: {order.first_name} {order.last_name}')
    print(f'O łącznej wartości: {order.total_price}')
    print('Zamówione produkty:')
    for product in order.product_list:
        print('\t', end='')
        print_product(product)
    print('=' * 20)
    print()


def print_product(product):
    print(f'Product: {product.name}, category: {product.category_name}, price: {product.price_per_unit}')


def run():
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

    # small_potato = Potato(species='Potato', size='small', price_per_unit=2)
    # big_potato = Potato(species='Potato', size='big', price_per_unit=6)
    # small_apple = Apple(species='Apple', size='small', price_per_unit=4)
    # medium_apple = Apple(species='Apple', size='medium', price_per_unit=7)
    # print(small_potato.species, small_potato)
    # print(big_potato.species, big_potato)
    # print(small_apple.species, small_apple)
    # print(medium_apple.species, medium_apple)
    #
    # cookies = Product(name="cookie", category_name="food", price_per_unit=3.5)
    # empty_order = Order(first_name='Marek', last_name='Garbowski')
    # order_1 = Order(first_name='Adam', last_name='Słodowy', product_list=[cookies, cookies, cookies])
    # print(cookies)
    # print_order(empty_order)
    # print_order(order_1)


if __name__ == '__main__':
    run()
