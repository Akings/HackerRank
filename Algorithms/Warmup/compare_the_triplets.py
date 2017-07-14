#!/bin/python3


def solve(alice, bob):
    alice_score, bob_score = 0, 0
    for a, b in zip(alice, bob):
        if a > b:
            alice_score += 1
        elif a < b:
            bob_score += 1
    return alice_score, bob_score


def main():
    alice = map(int, input().strip().split(' '))
    bob = map(int, input().strip().split(' '))
    result = solve(alice, bob)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
