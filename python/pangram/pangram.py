import re


def is_pangram(sentence):
    letters = set(re.findall('[a-z]', sentence.lower()))

    return len(letters) == 26
