scores_input = {
    1: "A, E, I, O, U, L, N, R, S, T",
    2: "D G",
    3: "B C M P",
    4: "F H V W Y",
    5: "K",
    8: "J X",
    10: "Q, Z"
}

score_per_upcase_letter = {}
for score, letters in scores_input.items():
    for letter in letters:
        score_per_upcase_letter[letter] = score


def score(word):
    return sum([score_per_upcase_letter[letter.upper()] for letter in word])
