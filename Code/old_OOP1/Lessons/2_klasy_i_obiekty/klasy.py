class Student:
    pass


class Grade:
    pass


class School:
    pass


if __name__ =='__main__':
    student_marek = Student()

    grade_a = Grade()
    grade_b = Grade()

    my_school = School()

    print(student_marek)
    print(grade_a, grade_b)
    print(my_school)

print('type(student_marek):', type(student_marek))
print('type(grade_a):', type(grade_a))
print('type(grade_b):', type(grade_b))
print('type(my_school):', type(my_school))

all_students = [Student(), Student(), Student(), Student()]
print(all_students)
print(all_students[0])

grades = {
    1: Grade(),
    2: Grade(),
    3: Grade(),
    4: Grade()
}

print(grades)
