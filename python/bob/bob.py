import re

def hey(phrase):
    if re.search('\!', phrase):
        if re.search('\?', phrase):
            return "Sure."
        elif phrase.isupper():
            return 'Whoa, chill out!'
        else:
            return "Whatever."

    if phrase.strip() == "":
        return "Fine. Be that way!"
    elif re.search('\n', phrase):
        return "Whatever."

    if phrase.strip()[-1] == "?":
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    

    if phrase.isupper():
        return "Whoa, chill out!"


    return "Whatever."