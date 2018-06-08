import os
import random
from string import ascii_uppercase


class Robot(object):
    def __init__(self):
        self.name = self._random_name()

    def _random_name(self):
        two_letters = [random.choice(ascii_uppercase) for _ in range(2)]
        three_digits = [str(random.randint(0, 9)) for _ in range(3)]

        return "".join(two_letters + three_digits)

    def reset(self):
        random.seed(os.urandom)

        self.__init__()
