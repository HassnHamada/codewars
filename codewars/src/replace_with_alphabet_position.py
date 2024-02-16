# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/py

def alphabet_position(text):
    result = ""
    for char in text:
        if char.isalpha():
            result += str(ord(char.lower()) - 96) + " "
    return result.strip()
