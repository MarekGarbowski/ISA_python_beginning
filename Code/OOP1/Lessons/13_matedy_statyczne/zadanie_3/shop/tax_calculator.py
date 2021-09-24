
class TaxCalculator:
    FRUITS_AND_VEGGIES = 0.05
    FOOD = 0.08
    OTHER = 0.2

    def __init__(self, item, group):
        self.item = item
        self.group = group

        if group == "FRUITS_AND_VEGGIES":
            return item * (1 + TaxCalculator.FRUITS_AND_VEGGIES)
        if group == 'FOOD':
            return item * (1 + TaxCalculator.FOOD)
        else:
            return item * (1 + TaxCalculator.OTHER)
