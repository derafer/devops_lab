def sort_inc(number):
    """ sorting digits in a number(> 0), to get largest version of it """
    number = str(number)
    sorting = list(map(int, number))
    sorting.sort(reverse=True)
    a = [str(i) for i in sorting]
    result = int("".join(a))
    return result


def sort_dec(number):
    """ sorting digits in a number (>0), to get smallest version of it """
    number = str(number)
    sorting = list(map(int, number))
    sorting.sort()
    nyliki = sorting.count(0)
    if nyliki > 0:
        sorting[0], sorting[nyliki] = sorting[nyliki], sorting[0]
    a = [str(i) for i in sorting]
    result = int("".join(a))
    return result


def summing(a, b):
    if a < 0:
        a *= -1
        large = sort_inc(a)
        large *= -1
    else:
        large = sort_inc(a)
    if b < 0:
        b *= -1
        small = sort_dec(b)
        small *= -1
    else:
        small = sort_dec(b)
    return large - small


if __name__ == '__main__':
    expense = int(input("Type your expenses: "))
    income = int(input("Type your income: "))
    print(summing(expense, income))
