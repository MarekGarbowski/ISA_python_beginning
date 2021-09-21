
class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print('To ja - metoda.')

    def print_self(self):
        print('czym jest self', self)
        print('Jest tutaj dostęp do name', self.name)

    def do_all_work(self):
        print('Teraz się napracuję...')
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        print('Koniec')

    def do_piece_of_work(self):
        print('Robota')


def run():
    student = Student(name='Marek')
    student.print_something()
    student.print_self()
    student.do_all_work()


if __name__ == "__main__":
    run()
