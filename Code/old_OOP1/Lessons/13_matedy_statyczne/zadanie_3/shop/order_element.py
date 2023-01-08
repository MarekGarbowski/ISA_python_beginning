from tax_calculator import TaxCalculator


class OrderElement:

    def __init__(self, product, quantity, group):
        self.group = group
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        item = self.product.unit_price * self.quantity
        total = TaxCalculator(item, self.group)
        return total

    def __str__(self):
        self.product.__str__()
        print(f"\t\t x {self.quantity}")
