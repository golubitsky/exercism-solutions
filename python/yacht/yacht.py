# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    """
    Category            Score                   Example
    Ones            1 × number of ones      1 1 1 4 5 scores 3
    Twos            2 × number of twos      2 2 3 4 5 scores 4
    Threes          3 × number of threes    3 3 3 3 3 scores 15
    Fours           4 × number of fours     1 2 3 3 5 scores 0
    Fives           5 × number of fives     5 1 5 2 5 scores 15
    Sixes           6 × number of sixes     2 3 4 5 6 scores 6
    Full House      Total of the dice       3 3 3 5 5 scores 19
    Four of a Kind  Total of the four dice  4 4 4 4 6 scores 16
    Little Straight 30 points               1 2 3 4 5 scores 30
    Big Straight    30 points               2 3 4 5 6 scores 30
    Choice          Sum of the dice         2 3 3 4 6 scores 18
    Yacht           50 points               4 4 4 4 4 scores 50
    """
    sorted_dice = sorted(dice)

    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
    elif ONES <= category <= SIXES:
        return dice.count(category) * category
    elif category == FULL_HOUSE:
        for d in dice:
            if not (2 <= dice.count(d) <= 3):
                return 0
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for d in dice:
            if dice.count(d) >= 4:
                return d * 4
    elif category == LITTLE_STRAIGHT:
        if sorted_dice == [1, 2, 3, 4, 5]:
            return 30
    elif category == BIG_STRAIGHT:
        if sorted_dice == [2, 3, 4, 5, 6]:
            return 30
    elif category == CHOICE:
        return sum(dice)
    return 0
