class Garden(object):
    _plants = {
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets',
        'G': 'Grass'
    }
    _plants_per_student_per_row = 2
    _default_students = ['Alice', 'Bob', 'Charlie', 'David',
                         'Eve', 'Fred', 'Ginny', 'Harriet',
                         'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=_default_students):
        self.rows = diagram.split('\n')
        self.students = sorted(studenty)

    def plants(self, student):
        i = self.students.index(student)
        return list(map(lambda code: self._plants[code], [
            self.rows[0][i * self._plants_per_student_per_row],
            self.rows[0][i * self._plants_per_student_per_row + 1],
            self.rows[1][i * self._plants_per_student_per_row],
            self.rows[1][i * self._plants_per_student_per_row + 1],
        ]))
