import string
import re

index_backwards = {}
for i, letter in enumerate(string.ascii_lowercase):
    index_backwards[letter] = len(string.ascii_lowercase) - i - 1


def encode_char(char):
    if char.lower() not in index_backwards:
        return char

    encoded_index = index_backwards[char.lower()]
    return string.ascii_lowercase[encoded_index]


def remove_spaces(string):
    return re.sub('\s', '', string)


def encode(plain_text):
    # only encode letters and spaces
    clean = re.sub('[^\w\s]', '', plain_text)
    encoded = "".join(list(map(lambda char: encode_char(char), clean)))

    # format into groups of 5 chars separated by single space
    encoded_no_spaces = remove_spaces(encoded)
    groups_of_five = [encoded_no_spaces[i:i+5]
                      for i in range(0, len(encoded_no_spaces), 5)]

    return " ".join(groups_of_five)


def decode(ciphered_text):
    clean = remove_spaces(ciphered_text)

    return "".join(list(map(lambda char: encode_char(char), clean)))
