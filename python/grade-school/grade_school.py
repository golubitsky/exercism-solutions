class School(object):
    def __init__(self, name):
        num_grades = 9
        self._grades = [[] for _ in range(num_grades)]
        self.name = name

    def _get_grade_by_external_index(self, n):
        return self._grades[n - 1]

    def add(self, student, grade):
        self._get_grade_by_external_index(grade).append(student)

    def grade(self, grade):
        return list(self._get_grade_by_external_index(grade))

    def sort(self):
        """
            For all grades that have students returns a tuple generator:
            (grade, (sorted_students_in_grade))
        """
        grades_with_students = []
        for grade, students in enumerate(self._grades):
            if len(students) == 0:
                continue
            # we store indexed at 0; e.g. grade 1 @ index 0
            grades_with_students.append((grade + 1, tuple(sorted(students))))

        for x in sorted(grades_with_students):
            yield x
