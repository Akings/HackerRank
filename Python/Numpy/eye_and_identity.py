import numpy as np


def main():
    N, M = map(int, input().split())
    print(np.eye(N, M, k=0))


if __name__ == '__main__':
    main()
