from estudent.school import School


def run_example():
    school = School.create_school_with_students("Hogwart")
    student = school.students[0]
    student.add_final_grade(4)
    print(school)
    print(f'W szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów')

    # print(student._final_grades)
    # school._promote_lucky_students()


if __name__ == '__main__':
    run_example()
