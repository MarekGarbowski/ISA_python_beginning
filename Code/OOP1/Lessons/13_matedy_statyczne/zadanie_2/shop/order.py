import random

from order_element import OrderElement
from product import Product


class Order:
    MAX_ORDER_ELEMENTS = 10

    def __init__(self, client_first_name, client_last_name, order_elements=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for product in self._order_elements:
            total_price += product.calculate_price()
        return total_price

    def add_product_to_order(self, product, quantity):
        new_element = OrderElement(product, quantity)
        self._order_elements.append(new_element)
        self.total_price = self._calculate_total_price()

    def __len__(self):
        return len(self._order_elements)

    def __str__(self):
        print("=" * 20)
        print(f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}")
        print(f"O łącznej wartości: {self.total_price} PLN")
        print("Zamówione produkty:")
        for product in self._order_elements:
            print("\t", end="")
            product.__str__()
        print(f'Liczba produktów w zamówieniu: {self.__len__()}')
        print("=" * 20)
        print()

    @staticmethod
    def generate_order():
        number_of_product = random.randint(1, Order.MAX_ORDER_ELEMENTS)
        order_elements = []
        for product_number in range(number_of_product):
            product_name = f"Produkt-{product_number}"
            category_name = "Inne"
            unit_price = random.randint(1, 30)
            product = Product(product_name, category_name, unit_price)
            quantity = random.randint(1, 10)
            order_elements.append(OrderElement(product, quantity))

        order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", order_elements=order_elements)
        return order
