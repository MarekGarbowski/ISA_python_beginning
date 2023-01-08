import random

from estudent.school import create_school_with_students


def run():
    school = create_school_with_students('Hogwart')
    school.print_self()

    for student in school.students:
        student.promote()
    school.print_self()
    print('=' * 20)

    for student in school.students:
        final_grade = random.randint(1, 4)
        student.add_final_grade(final_grade)
    school.print_self()


if __name__ == '__main__':
    run()
