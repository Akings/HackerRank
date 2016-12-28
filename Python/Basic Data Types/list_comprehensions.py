#!/usr/bin/env python
"""
====
Task
====
Let's learn about list comprehensions! You are given three integers X,Y and Z
representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on
a 3D grid where the sum of i+j+k is not equal to N.
Here, 0 <= i <= X, 0 <= j <= Y, 0 <= k <= Z,

============
Input Format
============
Four integers X,Y,Z and N each on four separate lines, respectively.

=============
Output Format
=============
Print the list in lexicographic increasing order.

============
Sample Input
============
Input::
    1
    1
    1
    2

=============
Sample Output
=============
Output::
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

=========
Editorial
=========
--------
Python 2
--------
Solution::
    a, b, c, n = [int(raw_input()) for _ in xrange(4)]
    print [[x,y,z] for x in xrange(a + 1)
                   for y in xrange(b + 1)
                   for z in xrange(c + 1) if x + y + z != n]
"""

from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def list_comprehension(x, y, z, n):
    return [[i, j, k] for i in range(x+1)
            for j in range(y+1)
            for k in range(z+1)
            if i + j + k != n]


if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    possible_coordinates = list_comprehension(X, Y, Z, N)
    print(possible_coordinates)
