def prime_factors(natural_number):
    remainder = natural_number
    i = 2
    factors = []
    while remainder > 1:
        if remainder % i == 0:
            remainder /= i
            factors.append(i)
        else:
            i += 1

    return factors
