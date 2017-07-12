import numpy as np


def main():
    rows = []
    n, m = map(int, input().split(' '))
    for _ in range(n):
        row = input().split(' ')
        rows.append(row)
    arr = np.array(rows, int)
    print(np.prod(np.sum(arr, axis=0)))


if __name__ == '__main__':
    main()
