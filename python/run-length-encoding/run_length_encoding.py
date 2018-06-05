import re
import itertools


def decode(string):
    decoded = ""

    for n, char in re.findall('(\d+)?([a-z]{1}|\s)', string, re.IGNORECASE):
        if n:
            decoded += char * int(n)
        else:
            decoded += char

    return decoded


def encode(string):
    groups = [''.join(value) for key, value in itertools.groupby(string)]

    encoded = ""
    for group in groups:
        if len(group) == 1:
            encoded += group[0]
        else:
            encoded += f"{len(group)}{group[0]}"

    return encoded
