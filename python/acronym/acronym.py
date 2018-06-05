import re

def abbreviate(words):
    split = words.split()
    first_chars_list_of_lists = list(map(lambda word: re.findall('(\w)\w+', word), split))
    first_chars = [ltr for sublist in first_chars_list_of_lists for ltr in sublist]

    return "".join(first_chars).upper()
