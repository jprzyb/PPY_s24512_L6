import math


def isPerfect(n):
    sum = 0
    for divisor in range(n, 0, -1):
        if n % divisor == 0:
            sum += divisor
    return sum == n


def checkPerfection(my_list):
    dictionary = {}
    # dictionary.pop(0)
    for _ in my_list:
        dictionary[_] = isPerfect(_)
    return dictionary


def __main__():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    print(checkPerfection(my_list))


if __name__ == '__main__':
    __main__()
