# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    nums = list(map(int, list(str(n))))
    total = sum(j**(i+p) for i, j in enumerate(nums))
    if total % n:
        return -1
    return total // n
