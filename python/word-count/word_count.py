from collections import Counter
import re


def word_count(phrase):
    lower = phrase.lower()

    # Words
    matches = re.findall('(\'?([a-z\d]+\'?[a-z])\'?)', lower)
    # get first group
    words = list(map(lambda m: m[1], matches))

    # Numbers
    numbers = re.findall('\d+', lower)

    # Count
    d = dict(Counter(words + numbers))
    print(d)
    return d
