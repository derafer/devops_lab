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
    if sorting.count(0) > 0:
        sorting[0], sorting[sorting.count(0)] = sorting[sorting.count(0)], sorting[0]
    a = [str(i) for i in sorting]
    result = int("".join(a))
    return result


expense = int(input("Type your expenses: "))
income = int(input("Type your income: "))

# preparing first number
if expense < 0:
    expense *= -1
    large = sort_inc(expense)
    large *= -1
else:
    large = sort_inc(expense)

# preparing second number
if income < 0:
    income *= -1
    small = sort_dec(income)
    small *= -1
else:
    small = sort_dec(income)

print(large - small)
