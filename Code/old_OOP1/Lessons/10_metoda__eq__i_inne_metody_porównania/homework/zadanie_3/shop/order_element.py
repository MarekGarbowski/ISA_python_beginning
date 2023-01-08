class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.product.unit_price * self.quantity

    def __str__(self):
        self.product.__str__()
        print(f"\t\t x {self.quantity}")
