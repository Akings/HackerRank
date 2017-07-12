import numpy as np


def main():
    array = np.array(input().split(' '), float)
    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))


if __name__ == '__main__':
    main()
