import operator


if __name__ == '__main__':
    students_grades = []
    grades = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grades.append([name, score])
        grades.add(score)
    student_grades = sorted(students_grades, key=operator.itemgetter(1))
    second_lowest_grade = sorted(grades)[1]
    names = [name for name, grade in students_grades if grade == second_lowest_grade]
    for name in sorted(names):
        print(name)
