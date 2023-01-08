from estudent.school import School
from estudent.config import Config


def run_example():
    school = School.create_school_with_students("Hogwart")
    student = school.students[0]
    student.add_final_grade(4)
    print(school)
    print(f'W szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów')

    print(Config.ADMINISTRATION_EMAIL)
    print(Config.DATABASE_URL)


if __name__ == '__main__':
    run_example()
