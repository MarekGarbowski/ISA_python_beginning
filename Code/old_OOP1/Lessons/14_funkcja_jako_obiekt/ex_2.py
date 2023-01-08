import random


def say_hello():
    print('Hello world!')


def say_goodbye():
    print('Good bye!')


def randomise_func(firs_func, sec_func):
    number = random.randint(1, 2)
    if number == 1:
        return firs_func
    return sec_func


def run():
    hello_or_good_bye = randomise_func(say_hello, say_goodbye)
    hello_or_good_bye()


if __name__ == '__main__':
    run()
