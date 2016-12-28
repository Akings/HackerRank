#!/usr/bin/env python
"""
====
Task
====
Read two integers and print two lines. The first line should contain integer
division, a//b. The second line should contain float division, a/b.

You don't need to perform any rounding or formatting operations.

============
Input Format
============
The first line contains the first integer, aa. The second line contains the
second integer, bb.

=============
Output Format
============
Print the two lines as described above.
============
Sample Input
============
Input::
    4
    3

=============
Sample Output
=============
Output::
    1
    1.3333333333333333
"""


from __future__ import division, print_function


def main():
    """Division challenge."""
    first_int = int(raw_input())
    second_int = int(raw_input())
    print(first_int // second_int)
    print(first_int / second_int)


if __name__ == '__main__':
    main()
