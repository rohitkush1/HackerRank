n = int(input())

students = {}

for student in range(n):
    name, *marks = input().split()
    student_marks = list(map(float, marks))
    students[name] = student_marks

query_name = input()
total_marks = 0

for subject_mark in students[query_name]:
    total_marks += subject_mark
    marks_average = total_marks/3

print("{0:.2f}".format(marks_average))
