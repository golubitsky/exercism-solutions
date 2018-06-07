import re
import random


class Cipher(object):
    first_char_in_alphabet = 'a'
    last_char_in_alphabet = 'z'
    alphabet_length = 26

    def __init__(self, key=None):
        self.key = self._generate_key(key)

    def _generate_key(self, key_input):
        """Key stores letters whose ords are used to shift text input.
        It would be more efficient to store the ords themselves, but one of the tests necessitates
        that we store letters.
        """
        if not key_input:
            # generate random alphabetic key
            start = ord(self.first_char_in_alphabet)
            key = [chr(start + random.randint(0, self.alphabet_length - 1))
                   for _ in range(100)]
            return "".join(key)

        is_all_lowercase = re.sub('[^a-z]', '', key_input) == key_input

        if not is_all_lowercase:
            raise ValueError('Key must be lowercase alphabetic characters.')
        else:
            return key_input

    def _encode_char(self, char_to_encode, char_to_encode_with, decode):
        """ Boolean decode reverses the operation.
        """
        switch = -1 if decode else 1

        shift = switch * (ord(char_to_encode_with) -
                          ord(self.first_char_in_alphabet))
        target_ord = ord(char_to_encode) + shift

        # ensure target is in range
        if target_ord > ord(self.last_char_in_alphabet):
            target_ord -= self.alphabet_length
        elif target_ord < ord(self.first_char_in_alphabet):
            target_ord += self.alphabet_length

        return chr(target_ord)

    def encode(self, text, decode=False):
        """ Uses key to encode text.
        Boolean decode reverses the operation.
        """
        encoded = []
        key_index = 0

        for char in text:
            encoded_char = self._encode_char(char, self.key[key_index], decode)
            encoded.append(encoded_char)

            key_index += 1
            if key_index == len(self.key):
                # loop key
                key_index = 0

        return "".join(encoded)

    def decode(self, text):
        decode = True

        return self.encode(text, decode)


class Caesar():
    def __init__(self):
        self.cipher = Cipher("d")

    def _clean(self, text):
        return re.sub('[^a-z]', '', text.lower())

    def encode(self, text):
        return self.cipher.encode(self._clean(text))

    def decode(self, text):
        return self.cipher.decode(self._clean(text))
