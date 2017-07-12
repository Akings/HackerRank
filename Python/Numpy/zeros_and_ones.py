import numpy as np


def main():
    size = tuple(map(int, input().split()))
    print(np.zeros(size, dtype=np.int))
    print(np.ones(size, dtype=np.int))


if __name__ == '__main__':
    main()
