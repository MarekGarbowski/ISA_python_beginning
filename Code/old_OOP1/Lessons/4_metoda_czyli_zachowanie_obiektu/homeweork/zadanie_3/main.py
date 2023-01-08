from shop.apple import Apple
from shop.potato import Potato
from shop.order import generate_order


def run_homework():
    # small_apple = Apple(species_name='red apple', size='small', price=2.4)
    # fresh_potato = Potato(species_name='Globo', size='medium', price=3.38)
    # print(f'10 kg małych jabłek kosztuje: {small_apple.calculate_price(10)}')
    # print(f'24 kg młodych ziemniaków kosztuje: {fresh_potato.calculate_price(24)}')

    first_order = generate_order()
    first_order.print_self()
    second_order = generate_order()
    second_order.print_self()

    # green_apple = Apple(species_name="Green", size="M", price=3.5)
    # red_apple = Apple(species_name="Red", size="S", price=2.8)
    # print(green_apple.species_name, green_apple)
    # print(red_apple.species_name, red_apple)

    # old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    # print(old_potato.species_name, old_potato)

    # first_order = generate_order()
    # order.print_order(first_order)
    # second_order = generate_order()
    # order.print_order(second_order)


if __name__ == '__main__':
    run_homework()
