import numpy as np


def main():
    n, m = map(int, input().split(' '))
    arr = np.array([input().strip().split(' ') for _ in range(n)], int)
    print(np.max(np.min(arr, axis=1)))


if __name__ == '__main__':
    main()
