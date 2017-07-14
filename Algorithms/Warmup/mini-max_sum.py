#!/bin/python3


def main():
    arr = list(map(int, input().strip().split(' ')))
    arr = sorted(arr)
    print(sum(arr[:-1]), sum(arr[1:]))


if __name__ == '__main__':
    main()
