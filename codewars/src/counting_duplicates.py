# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

from collections import Counter


def duplicate_count(text):
    text = Counter(text.lower())
    return sum(1 for i in text.values() if i > 1)
