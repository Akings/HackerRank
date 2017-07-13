import numpy as np


def main():
    n = int(input())
    arr = np.array([input().strip().split(' ') for _ in range(n)], float)
    print(np.linalg.det(arr))


if __name__ == '__main__':
    main()
