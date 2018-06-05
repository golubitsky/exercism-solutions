from collections import Counter


def detect_anagrams(word, candidates):
    results = []

    lower_word = word.lower()
    for candidate in candidates:
        if len(candidate) != len(word):
            continue

        lower_candidate = candidate.lower()
        if Counter(lower_candidate) == Counter(lower_word):
            if lower_candidate != lower_word:
                results.append(candidate)

    return results
