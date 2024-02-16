# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    errors = 0
    for c in s:
        if c not in "abcdefghijklm":
            errors += 1
    return "{}/{}".format(errors, len(s))
