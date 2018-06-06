first_square = 1
last_square = 64


def validate(square):
    if not first_square <= square <= last_square:
        raise ValueError(f"Square {square} is not on the chess board.")


def on_square(square):
    validate(square)

    return 2 ** (square - 1)


def total_after(square):
    validate(square)

    return int("1" * square, base=2)
