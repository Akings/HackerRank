import numpy as np


def main():
    n = int(input())
    arr1 = np.array([input().strip().split(' ') for _ in range(n)], int)
    arr2 = np.array([input().strip().split(' ') for _ in range(n)], int)
    print(np.dot(arr1, arr2))


if __name__ == '__main__':
    main()
