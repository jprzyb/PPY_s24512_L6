def primary_numbers(limit=None):
    if limit is None:
        limit = 380

    my_list = [True] * limit
    my_list[0] = False
    my_list[1] = False

    for i in range(2, int(limit ** 0.5)):
        if not my_list[i]:
            continue
        for j in range(i * i, limit, i):
            my_list[j] = False

    for i in range(2, limit):
        if my_list[i]:
            print(i)


def __main__():
    limit = (input("Enter a limit: "))
    if limit == "":
        primary_numbers()
    else:
        primary_numbers(int(limit) +1)


if __name__ == '__main__':
    __main__()
