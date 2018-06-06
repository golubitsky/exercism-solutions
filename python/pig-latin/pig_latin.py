import re


vowel_rule_regex = '^xr|yt|a|e|i|o|u'
consonant_rule_regex = "^squ|qu|sch|ch|sh|thr|th|rh|[bcdfghjklmnpqrstvwxyz]"
suffix = "ay"


def vowel_rule(word):
    return word + suffix


def consonant_rule(word, move_to_end_length):
    return word[move_to_end_length:] + word[:move_to_end_length] + suffix


def translate_word(word):
    if re.match(vowel_rule_regex, word):
        return vowel_rule(word)
    else:
        length = len(re.match(consonant_rule_regex, word)[0])
        return consonant_rule(word, length)


def translate(text):
    return " ".join([translate_word(word) for word in text.split()])
