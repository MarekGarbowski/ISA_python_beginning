import random

# class Student:
#
#     def __init__(self):
#         print('Powstaje nowy obiekt')
#
#
# if __name__ == '__main__':
#     student = Student()

# class Student:
#
#     def __init__(self):
#         self.first_name = 'Marek'
#         # self.first_name = input('Podaj imię: ')
#         self.last_name = 'Garbowski'
#         self.age = 44
#
#
# def run_example():
#     student = Student()
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
#     student.first_name = 'Jakub'
#     student.last_name = 'Kowalski'
#     student.age = 54
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
#
#
# if __name__ == '__main__':
#     run_example()


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


# class School:
#
#     def __init__(self, name, students):
#         self.name = name
#         self.students = students

# class School:
#
#     def __init__(self, name, students):
#         self.name = name
#         if len(students) > 10:
#             students = students[:10]
#             self.students = students

# class School:
#
#     def __init__(self, name, students=None):
#         self.name = name
#         if students is None:
#             students = []
#             self.students = students

class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students
        promote_lucky_students(students)


def promote_lucky_students(students):
    for index, student in enumerate(students):
        if index % 3 == 0:
            promote_student(student)


def print_student(student):
    print(f'student: {student.first_name} {student.last_name}, promoted: {student.promoted}')


# Side effect w klasie
def assign_student_to_school(school, student):
    school.students.append(student)


def promote_student(student):
    student.promoted = True


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 10)
    students = []
    for student_number in range(number_of_students):
        first_name = f'Student-{student_number}'
        last_name = 'Smith'
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    # school_without_students = School('Pusta szkoła')
    # first_student = Student(first_name='Marek', last_name='Garbowski')
    # assign_student_to_school(school_without_students, first_student)
    #
    # for student in school_without_students.students:
    #     print_student(student)

    school = create_school_with_students('Zadupiewo')
    print(school)
    for student in school.students:
        print_student(student)

    # student = Student(first_name="Marek", last_name='Garbowski')
    # print_student(student)
    #
    # other_student = Student('Adam', 'Słodowy')
    # print_student(other_student)
    #
    # promote_student(student)
    # print_student(student)


if __name__ == '__main__':
    run_example()
