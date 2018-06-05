def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError('.+')

    slices = []
    for i in range(len(series) - length + 1):
        slices.append(series[i:i + length])

    return slices
