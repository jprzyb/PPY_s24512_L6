import math


def calc(n):
    return math.factorial(2*n)/(math.factorial(n+1) * math.factorial(n))


def catalanNumber(n, factor):
    if factor == "p":
        for i in range(0, n + 1, 2):
            print(f"n={i}/{n}, catalan={calc(i)}")
    if factor == "n":
        for i in range(1, n + 1, 2):
            print(f"n={i}/{n}, catalan={calc(i)}")
    if factor == "a":
        for i in range(1, n + 1, 1):
            print(f"n={i}/{n}, catalan={calc(i)}")


def __main__():
    n = int(input("Enter number: "))
    factor = input("Enter factor (pick one: p,n,a): ")
    catalanNumber(n, factor)


if __name__ == '__main__':
    __main__()
