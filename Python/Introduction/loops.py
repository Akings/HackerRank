#!/usr/bin/env python2
"""
====
Task
====
Read an integer N. For all non-negative integers i<N, print i^2. See the
sample for details.

============
Input Format
============
The first and only line contains the integer, N.

===========
Constraints
===========
1≤N≤20

=============
Output Format
=============
Print N lines, one corresponding to each i.

============
Sample Input
============
Input::
    5

=============
Sample Output
=============
Output::
    0
    1
    4
    9
    16
"""


from __future__ import print_function


def main():
    """Loops challenge."""
    loop_len = int(raw_input())
    for i in range(loop_len):
        print(i ** 2)


if __name__ == '__main__':
    main()
