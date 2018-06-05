import math


class Allergies(object):
    allergy_values = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score):
        self.score = score
        self.cached_list = None

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        if self.cached_list:
            return self.cached_list

        self.cached_list = []
        score_left = self.score
        while score_left != 0:
            biggest_power = math.floor(math.log2(score_left))

            biggest = 2 ** biggest_power
            if biggest in self.allergy_values:
                self.cached_list.append(self.allergy_values[biggest])

            score_left -= biggest

        return self.cached_list
