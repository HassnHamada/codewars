# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(array):
    if not array:
        return []

    result = []
    while array:
        result += array.pop(0)

        for row in array:
            result.append(row.pop())

        if array:
            result += array.pop()[::-1]

        for row in array[::-1]:
            result.append(row.pop(0))

    return result
