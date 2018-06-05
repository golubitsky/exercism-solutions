from collections import defaultdict
import re

def is_isogram(string):
    count = defaultdict(lambda: 0)
    for letter in re.sub('[^a-z]*', '', string.lower()):
        count[letter] += 1
        if count[letter] > 1:
            return False

    return True