# https://www.codewars.com/kata/526989a41034285187000de4/train/python

def ips_between(start, end):
    start_nums = list(map(int, start.split(".")))
    end_nums = list(map(int, end.split(".")))
    start_nums.reverse(), end_nums.reverse()
    nums = zip(start_nums, end_nums)

    def calc():
        for i, (j, k) in enumerate(nums):
            yield (k - j) * (256 ** i)
    return sum(calc())
