class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [list(map(int, line.split()))
                     for line in matrix_string.split('\n')]

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return [row[index] for row in self.rows]
