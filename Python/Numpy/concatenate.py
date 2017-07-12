import numpy as np


def main():
    rows1, rows2, columns = map(int, input().split())
    array1 = np.array([input().strip().split(' ') for _ in range(rows1)], int)
    array2 = np.array([input().strip().split(' ') for _ in range(rows2)], int)
    print(np.concatenate((array1, array2), 0))


if __name__ == '__main__':
    main()
