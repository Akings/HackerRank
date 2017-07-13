import numpy as np


def main():
    coefs = np.array(input().strip().split(' '), float)
    x = float(input())
    print(np.polyval(coefs, x))


if __name__ == '__main__':
    main()
