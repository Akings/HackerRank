if __name__ == '__main__':
    input()
    first_set = set(int(x) for x in input().split())
    input()
    second_set = set(int(x) for x in input().split())
    symmetric_difference = first_set.symmetric_difference(second_set)
    for item in sorted(symmetric_difference):
        print(item)
