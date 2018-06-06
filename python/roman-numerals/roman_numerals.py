values = [1000, 500,  100,  50,  10,   5,  1]
romans = ['M',  'D',  'C', 'L', 'X', 'V', 'I']


def numeral(number):
    """
        Convert from Arabic to Roman numerals.
    """
    remainder = number
    converted = ""
    special_snowflakes = {"I", "X", "C"}

    for i, value in enumerate(values):
        number_of_this_char, remainder = remainder // value, remainder % value

        if romans[i] in special_snowflakes and number_of_this_char == 4:
            previous_char_requires_subtraction = len(
                converted) > 0 and converted[-1] == romans[i - 1]

            if previous_char_requires_subtraction:
                converted = converted[:-1] + f"{romans[i]}{romans[i - 2]}"
            else:
                converted += f"{romans[i]}{romans[i - 1]}"
        else:
            converted += romans[i] * number_of_this_char

    return converted
