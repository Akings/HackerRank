#!/usr/bin/env python
"""
====
Task
====
You are given the year, and you have to write a function to check if the year
is leap or not.
Note that you have to complete the function and remaining code is given as
template.

============
Input Format
============
Read y, the year that needs to be checked.

===========
Constraints
===========
1900 <= y <= 10^5

=============
Output Format
=============
Output is taken care of by the template. Your function must return a boolean
value (True/False)

============
Sample Input
============
Input::
    1990

=============
Sample Output
=============
Output::
    False

=========
Editorial
=========
--------
Python 2
--------
Solution::
    def is_leap(n):
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        if n % 4 == 0:
            return True
        return False

    print is_leap(input())

--------
Python 2
--------
Solution::
    def is_leap(year):
        return (year % 400 == 0) or (( year % 100 != 0) and (year % 4 == 0))

    print is_leap(input())

--------
Python 3
--------
Solution::
    def is_leap(n):
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        if n % 4 == 0:
            return True
        return False
"""


from __future__ import unicode_literals


def is_leap(year):
    leap = False
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    else:
        leap = True
    return leap
