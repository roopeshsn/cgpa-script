def collecting_input(courses):
    all_credits = []
    grade_points = []
    print(f'Please input your {courses} subjects Credits and Grade Points')
    for idx in range(courses):
        while True:
            try:
                credit = int(input(f'> credit {idx + 1} '))
                all_credits.append(credit)
            except ValueError:
                error()
            else:
                break
        while True:
            try:
                grade_point = int(input(f'> Grade Point {idx + 1} '))
                grade_points.append(grade_point)
            except ValueError:
                error()
            else:
                break;
    return all_credits, grade_points


def calculate_cgpa(courses, all_credits, grade_points):
    credit_multiplied_by_grade = []
    for idx in range(courses):
        credit_point = all_credits[idx] * grade_points[idx]
        credit_multiplied_by_grade.append(credit_point)
    total_credit_points = sum(credit_multiplied_by_grade)
    total_credit = sum(all_credits)
    cgpa = total_credit_points / total_credit
    return cgpa


def sum(list):
    total = 0
    for element in list:
        total = total + element
    return total

def error():
    print('The value entered by you is not a +ve number! Try again...')


if __name__ == '__main__':
    while True:
        try:
            courses = int(input('> How many subjects you have? '))
        except ValueError:
            error()
        else:
            break
    all_credits, grade_points = collecting_input(courses)
    cgpa = calculate_cgpa(courses, all_credits, grade_points)
    print(cgpa)


