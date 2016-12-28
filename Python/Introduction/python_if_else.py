#!/usr/bin/env python
"""
====
Task
====
Given an integer, n, perform the following conditional actions:
* If n is odd, print `Weird`
* If n is even and in the inclusive range of 2 to 5, print `Not Weird`
* If n is even and in the inclusive range of 6 to 20, print `Weird`
* If n is even and greater than 20, print `Not Weird`

============
Input Format
============
A single line containing a positive integer, n.

===========
Constraints
===========
1<=n<=100

=============
Output Format
=============
Print `Weird` if the number is weird; otherwise, print `Not Weird`.

==============
Sample Input 0
==============
Input::
    3

===============
Sample Output 0
===============
Output::
    Weird

=========
Editorial
=========
--------
Python 2
--------
Problem Setter's code::
    n = int(raw_input())
    if n % 2 == 1:
        print "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        print "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        print "Weird"
    else:
        print "Not Weird"

--------
Python 3
--------
Problem Setter's code::
    n = int(input())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
"""

from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def python_if_else(number):
    if (number % 2 != 0) or (6 <= number <= 20):
        print("Weird")
    elif (2 <= number <= 5) or (number > 20):
        print("Not Weird")


if __name__ == '__main__':
    N = int(input())
    python_if_else(N)
