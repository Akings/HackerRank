#!/usr/bin/env python
"""
====
Task
====
You have a record of N students. Each record contains the student's name,
and their percent marks in Maths, Physics and Chemistry. The marks can be
floating values. The user enters some integer NN followed by the names and
marks for N students. You are required to save the record in a dictionary
data type. The user then enters a student's name. Output the average
percentage marks obtained by that student, correct to two decimal places.

============
Input Format
============
The first line contains the integer N, the number of students. The next
N lines contains the name and marks obtained by that student separated by a
space. The final line contains the name of a particular student previously
listed.

=============
Output Format
=============
Print one line: The average of the marks obtained by the particular student
correct to 2 decimal places.

===========
Constraints
===========
2 <= N <= 10
0 <= Marks <= 100

============
Sample Input
============
Input::
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

=============
Sample Output
=============
Output::
    56.00

=========
Editorial
=========
Problem Tester's code::
    d={}
    for i in range(int(raw_input())):
        line=raw_input().split()
        d[line[0]]=sum(map(float,line[1:]))/3
    print '%.2f' % d[raw_input()]
"""
from __future__ import division, print_function


try:
    input = raw_input
except NameError:
    pass


def main():
    """Finding the percentage challenge."""
    number_of_students = int(input())
    students = {}
    for _ in range(number_of_students):
        input_string = input()
        input_list = input_string.split()
        students[input_list[0]] = input_list[1:]
    chosen_one = input()
    chosen_sum = sum(float(x) for x in students[chosen_one])
    chosen_average = round(chosen_sum / len(students[chosen_one]), 2)
    print("{0:.2f}".format(chosen_average))


if __name__ == '__main__':
    main()
