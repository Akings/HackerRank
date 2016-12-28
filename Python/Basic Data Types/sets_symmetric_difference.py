#!/usr/bin/env python
"""
====
Task
====
Given 2 sets of integers, M and N, print their symmetric difference in
ascending order. The term symmetric difference indicates those values that
exist in either M or N but do not exist in both.

============
Input Format
============
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

=============
Output Format
=============
Output the symmetric difference integers in ascending order, one per line.

============
Sample Input
============
Input::
    4
    2 4 5 9
    4
    2 4 11 12

=============
Sample Output
=============
Output::
    5
    9
    11
    12

=========
Editorial
=========
Solution::
    M = raw_input();m = raw_input().split()
    N = raw_input();n = raw_input().split()
    print "\n".join(sorted(list(set(m) ^ set(n)),key=int))
"""

from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def main():
    input()
    first_set = set(int(x) for x in input().split())
    input()
    second_set = set(int(x) for x in input().split())
    symmetric_difference = first_set.symmetric_difference(second_set)
    for item in sorted(symmetric_difference):
        print(item)

if __name__ == '__main__':
    main()
