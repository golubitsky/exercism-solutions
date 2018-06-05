import re

def verify(isbn):
    digits = re.findall('\d|X', isbn)
    if len(digits) != 10:
        return False

    total = 0
    check_digit = 'X'
    for i, digit in enumerate(digits):
        if digit == check_digit and i != 9:
            return False # check_digit can only be in last index
        elif digit == check_digit:
            total += ((10 - i) * 10)
        else:
            total += ((10 - i) * int(digit))

    
    return total % 11 == 0