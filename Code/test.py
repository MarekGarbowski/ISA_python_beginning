class Student:
    def __init__(self, student):
        self.student = student

    def print_s(self):
        print(f'To ja metoda {self.student}')


student = Student("Marek")
print(student)
student.print_s()
