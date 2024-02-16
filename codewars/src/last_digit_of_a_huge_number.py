# mhttps://www.codewars.com/kata/5518a860a73e708c0a000027/train/python

from codewars.wrong import wrong


@wrong
def last_digit(lst):
    if len(lst) == 0:
        return 1
    result = lst[-1]
    for x in range(len(lst) - 2, 0, -1):
        if result:
            result = max(result % 347011, 1)
        result = pow(lst[x], result)
    return pow(lst[0], result, 10)
