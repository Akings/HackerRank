#!/bin/python3


def birthdayCakeCandles(ar):
    ar = sorted(ar)
    return ar.count(ar[-1])


def main():
    _ = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = birthdayCakeCandles(ar)
    print(result)


if __name__ == '__main__':
    main()
