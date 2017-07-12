import numpy as np


def main():
    operations = [np.add, np.subtract, np.multiply, np.floor_divide, np.mod,
                  np.power]
    N, M = map(int, input().split(' '))
    array1 = np.array([input().split(' ') for _ in range(N)], int)
    array2 = np.array([input().split(' ') for _ in range(N)], int)
    for operation in operations:
        print(operation(array1, array2))


if __name__ == "__main__":
    main()
