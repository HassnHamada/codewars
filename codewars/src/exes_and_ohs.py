# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

from collections import Counter

def xo(s):
    s = Counter(s.lower())

    return s.get('x', 0) == s.get('o', 0)

