import re
import math


def _dimensions(clean_text):
    """Fit all chars in clean_text into a rectangle (rows x columns), such that:
        1. columns >= rows
        2. columns - rows <= 1
    """
    l = len(clean_text)
    if l == 1:
        return (1, 1)

    cols = math.ceil(math.sqrt(l))
    rows = cols - 1 if cols * (cols - 1) >= l else cols

    return (rows, cols)


def encode(plain_text):
    # Clean/Validate
    clean = re.sub('[^A-Za-z\d]', '', plain_text).lower()
    if not clean:
        return ''

    # Determine dimensions
    rows, cols = _dimensions(clean)

    # Split text into rectangle matrix
    col_i, row_i = 0, 0
    text_matrix = [''] * rows

    for char in clean:
        text_matrix[row_i] += char
        col_i += 1

        if col_i == cols:
            row_i += 1
            col_i = 0

    # Ensure all rows are of equal and expected length
    for i in range(len(text_matrix)):
        text_matrix[i] = text_matrix[i].ljust(cols)

    # Encode as transpose
    transposed = [''] * cols

    for row in text_matrix:
        for transposed_row, char in enumerate(row):
            transposed[transposed_row] += char

    return " ".join(transposed)
