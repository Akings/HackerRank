import numpy as np


def main():
    n, m = map(int, input().split(' '))
    arr = np.array([input().strip().split(' ') for _ in range(n)], int)
    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(np.std(arr))


if __name__ == '__main__':
    main()
