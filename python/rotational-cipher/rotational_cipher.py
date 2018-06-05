import string


def letter_indexes():
    indexes = {}
    for i, letter in enumerate(string.ascii_lowercase):
        indexes[letter] = i

    return indexes


def rotate(text, key):
    indexes = letter_indexes()

    rotated = ""
    for char in text:
        if char.lower() not in indexes:
            # not a letter, do not modify
            rotated += char
            continue

        start = indexes[char.lower()]
        target = (start + key) % len(indexes)

        if char.upper() == char:
            rotated += string.ascii_lowercase[target].upper()
        else:
            rotated += string.ascii_lowercase[target]

    return rotated
