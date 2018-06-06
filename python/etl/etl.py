def transform(legacy_data):
    scores = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            scores[letter.lower()] = score

    return scores
