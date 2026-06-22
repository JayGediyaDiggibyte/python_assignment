from collections import namedtuple

def average_marks(student_count, columns, student_data):
    Student = namedtuple("Student", columns)
    total_marks = 0
    for row in student_data:
        student = Student(*row.split())
        total_marks += int(student.MARKS)
    return round(total_marks / student_count, 2)