from estudent.school import School
from estudent.config import Config


def grades_avg_for_students(student):
    return student.grades_avg()


def run_example():
    school = School.create_school_with_students("Hogwart")
    students = school.students
    for student in students:
        print(student)
    print('-' * 20)

    # students.sort()
    students.sort(key=grades_avg_for_students)


if __name__ == '__main__':
    run_example()
