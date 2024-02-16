# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

def get_pins(observed):
    adjacent_keys = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }

    pins = []

    def backtrack(comb, next_pos):
        if len(comb) == len(observed):
            pins.append(comb)
            return

        possible_digits = adjacent_keys[observed[next_pos]]
        for d in possible_digits:
            backtrack(comb + d, next_pos + 1)

    backtrack("", 0)

    return pins
