def flatten(iterable):
    flattened = []
    for value in iterable:
        if value is None:
            continue

        if type(value) in {list, set, tuple}:
            flattened.extend(flatten(value))
        else:
            flattened.append(value)

    return flattened
