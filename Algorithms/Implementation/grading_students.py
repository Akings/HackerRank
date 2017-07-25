#!/usr/bin/env python3
"""
Editorial.
=========

Python 3::

    n = int(input().strip())
    for a0 in range(n):
        grade = int(input().strip())

        if grade >= 38:
            # Here, we are only ever calculating
            # 'grade mod 5' once:
            mod5 = grade % 5

            if mod5 >= 3:
                grade = grade + (5 - mod5)

        print(grade)
"""


def solve(grades):
    """Return rounded grades."""
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            multiple_of5 = 5 * (grade // 5 + 1)
            rounded_grade = multiple_of5 if multiple_of5 - grade < 3 else grade
            rounded_grades.append(rounded_grade)
    return rounded_grades


def main():
    n = int(input().strip())
    grades = [int(input().strip()) for _ in range(n)]
    result = solve(grades)
    print("\n".join(map(str, result)))


if __name__ == '__main__':
    main()
