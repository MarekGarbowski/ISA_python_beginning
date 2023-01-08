class Apple:

    def __init__(self, species_name, size, price, quantity):
        self.species_name = species_name
        self.size = size
        self.price = price
        self.quantity = quantity
        cp = quantity * price
        self.cp = cp

    # def calculate_price(self, quantity):
    #     return quantity * self.price

    def __repr__(self):
        return f'{self.cp}'
