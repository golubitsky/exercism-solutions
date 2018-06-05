def is_multiple(n, multiples):
    for m in multiples:
        if n % m == 0:
            return True


def sum_of_multiples(limit, multiples):
    total = 0

    for i in range(limit):
        if is_multiple(i, multiples):
            total += i

    return total
