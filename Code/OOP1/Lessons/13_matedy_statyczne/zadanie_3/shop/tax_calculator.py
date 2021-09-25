
class TaxCalculator:
    FRUITS_AND_VEGGIES = 0.05
    FOOD = 0.08
    OTHER = 0.2

    def __init__(self, item, group):
        self.item = item
        self.group = group
        self.tax_rate = 0

        if group == "FRUITS_AND_VEGGIES":
            tax_rate = item * (1 + TaxCalculator.FRUITS_AND_VEGGIES)
        elif group == 'FOOD':
            tax_rate = item * (1 + TaxCalculator.FOOD)
        else:
            tax_rate = item * (1 + TaxCalculator.OTHER)
        return tax_rate
