import re


class Luhn(object):
    def __init__(self, card_num):
        self.card_num = self._remove_spaces(card_num)

    def _remove_spaces(self, card_num):
        return re.sub('\s+', '', card_num)

    def _validate_format(self):
        """Strings of length 1 or less are not valid. Spaces are allowed in the input,
        but they should be stripped before checking. All other non-digit characters
        are disallowed. """
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            raise ValueError(
                "Card number is invalid (16 numeric characters, spaces allowed).")

    def _double_and_substract_nine_if_greater_than_nine(self, n):
        y = n * 2

        return y - 9 if y > 9 else y

    def is_valid(self):
        # validation
        try:
            self._validate_format()
        except ValueError as e:
            return False

        # reverse and process every second element
        reversed_card_num = self.card_num[::-1]

        # extract all values as digits
        to_process = [
            int(d) for d in re.findall('\d(\d)', reversed_card_num)]
        others = [int(d) for d in re.findall('(\d)\d', reversed_card_num)]

        # processing
        processed = [
            self._double_and_substract_nine_if_greater_than_nine(d) for d in to_process]

        # validity check
        return sum(others + processed) % 10 == 0
