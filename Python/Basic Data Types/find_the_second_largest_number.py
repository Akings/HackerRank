#!/usr/bin/env python
"""
You are given N numbers. Store them in a list and find the second largest
number.

Input Format
The first line contains N. The second line contains an array A[] of N integers
each separated by a space.

Constraints
2 <= N <= 10
-100 <= A[i] <= 100

Output Format
Output the value of the second largest number.

Sample Input
5
2 3 6 6 5

Sample Output
5

Editorial
n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -6000, -6000
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)
"""
from __future__ import print_function, unicode_literals


try:
    input = raw_input
except NameError:
    pass


def find_the_second_largest_number(arr):
    """Find the second largest number."""
    arr.sort(reverse=True)
    largest_number = arr[0]
    for number in arr:
        if number < largest_number:
            return number


if __name__ == '__main__':
    N = int(input())
    ARR = [int(number) for number in input().split()]
    print(find_the_second_largest_number(ARR))
