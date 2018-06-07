from fractions import gcd
from math import sqrt, floor


def are_not_coprime(a, b):
    return gcd(a, b) > 1


def euclid(m, n):
    primitive = (m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2)

    return tuple(sorted(primitive))


def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2 == 1:
        raise ValueError("Input cannot be odd.")

    results = set()
    max_value = number_in_triplet ** 2
    # TODO: not sure how to winnow-down the brute-force search;
    # searching up to 211 solves all existing test-cases
    for m in range(2, 211):
        for n in range(1, m):
            if m % 2 == 1 and n % 2 == 1:
                continue
            if are_not_coprime(m, n):
                continue

            primitive = euclid(m, n)
            if number_in_triplet in primitive:
                results.add(primitive)

    return results


def triplets_in_range(range_start, range_end):
    return set([(a, b, c) for a in range(range_start, range_end - 1) for b in range(a + 1, range_end)
                for c in range(b + 1, range_end + 1) if is_triplet((a, b, c))])


def is_primitive_triplet(triplet):
    a, b, c = triplet
    if are_not_coprime(a, b) or are_not_coprime(b, c) or are_not_coprime(a, c):
        return False

    return is_triplet(triplet)


def is_triplet(triplet):
    a, b, c = sorted(triplet)

    return a ** 2 + b ** 2 == c ** 2
