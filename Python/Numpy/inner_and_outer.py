import numpy as np


def main():
    arr1 = np.array(input().strip().split(' '), int)
    arr2 = np.array(input().strip().split(' '), int)
    print(np.inner(arr1, arr2))
    print(np.outer(arr1, arr2))


if __name__ == '__main__':
    main()
