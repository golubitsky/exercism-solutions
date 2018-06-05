ones = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine', 'ten']

teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', 'ten', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# no off by one adjustment necessary
postfix = ['', '', 'thousand', 'million', 'billion']


def split_into_digits(number):
    """
        Splits a number into its digits, maintaining order of digits.
        E.g.: 1456 -> [1, 4, 5, 6]
    """
    return list(map(int, str(number)))


def say_less_than_hundred(number):
    result = ''
    if 0 <= number <= 10:
        result = ones[number]
    elif number < 20:
        result = teens[number % 10]
    elif number < 100:
        digits = split_into_digits(number)
        for digit_pos, digit in enumerate(digits):
            if digit_pos == 0:
                result += tens[digit]
            elif digit_pos == 1 and digit != 0:
                result += f"-{ones[digit]}"

    return result


def say_less_than_thousand(number):
    """
    >>> say_less_than_thousand(810)
    'eight hundred and ten'
    """
    result = []
    if number < 100:
        result.append(say_less_than_hundred(number))
    elif number < 1000:
        hundreds_digit = split_into_digits(number)[0]
        result.append(ones[hundreds_digit])
        result.append('hundred')
        if number % 100 > 0:
            result.append('and')
            result.append(say_less_than_hundred(number % 100))

    return " ".join(result).strip()


def split_into_groups(number):
    """Splits a number into groups of digits.
    >>> split_into_groups(123)
    [123]
    >>> split_into_groups(15123)
    [15, 123]
    >>> split_into_groups(1e6)
    [1, 0, 0]
    """
    reversed_number = str(int(number))[::-1]
    chunks_of_reversed_number = [reversed_number[i:i + 3]
                                 for i in range(0, len(reversed_number), 3)]
    return list(map(lambda chunk: int(chunk[::-1] if chunk != '0.0' else 0), reversed(chunks_of_reversed_number)))


def should_add_and_after(i, groups):
    """Should add "and" after thousand, million, billion groups 
        if ones group != zero and all others are zero.
    >>> should_add_and_after(0, [1, 0, 0, 1]) # million and one
    True
    >>> should_add_and_after(0, [1, 1, 0, 1]) # million with thousands
    False
    >>> should_add_and_after(1, [1, 1, 0, 1]) # thousand and one
    True
    >>> should_add_and_after(0, [1, 0, 0, 0, 0]) # billion with no ones
    False
    >>> should_add_and_after(3, [1, 0, 0, 1]) # don't add after ones digit
    False
    >>> should_add_and_after(0, [1, 234]) # don't add for thousand and one
    False
    """
    is_ones_digit = i == len(groups) - 1
    if is_ones_digit:
        return False

    only_zeros_in_between = set(groups[i + 1:len(groups) - 1]) == {0}
    ones_present = groups[-1] != 0

    return ones_present and only_zeros_in_between


def say(number):
    if number >= 1e12 or number < 0:
        raise ValueError('.+')

    groups = split_into_groups(number)

    result = []
    for i, group in enumerate(groups):
        print(group)
        if group == 0 and i > 0:
            continue

        result.append(say_less_than_thousand(group))
        result.append(postfix[len(groups) - i])

        if should_add_and_after(i, groups):
            result.append('and')

    return " ".join(result).strip()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
