import numpy as np


def main():
    array = []
    N, M = input().strip().split(' ')
    for _ in range(int(N)):
        array.append(input().strip().split(' '))
    nparray = np.array(array, int)
    print(np.transpose(nparray))
    print(nparray.flatten())


if __name__ == '__main__':
    main()
