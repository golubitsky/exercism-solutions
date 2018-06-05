from functools import reduce
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def largest_product(series, size):
    # Errors and special-case logic
    if not 0 <= size <= len(series):
        raise ValueError('.+')
    if series == "":
        return 1
    if not str.isdigit(series):
        raise ValueError('.+')

    # Happy path
    largest = 0
    for i in range(len(series) - size + 1):
        cur_slice = series[i:i + size]
        cur_prod = prod(map(int, cur_slice))
        if cur_prod > largest:
            largest = cur_prod

    return largest
