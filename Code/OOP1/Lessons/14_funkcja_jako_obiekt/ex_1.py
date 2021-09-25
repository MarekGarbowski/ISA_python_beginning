
def say_hello(name):
    print(f'Hello {name}')


def calculate_something(x, y):
    return x + y


def run():
    hello_name = say_hello
    hello_name('Marek')
    calculation = calculate_something
    result = calculation(2, 6)
    print(result)


if __name__ == '__main__':
    run()
