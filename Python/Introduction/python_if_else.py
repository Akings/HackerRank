#!/usr/bin/env python3


def python_if_else(number):
    if (number % 2 != 0) or (6 <= number <= 20):
        print("Weird")
    elif (2 <= number <= 5) or (number > 20):
        print("Not Weird")


if __name__ == '__main__':
    N = int(input())
    python_if_else(N)
