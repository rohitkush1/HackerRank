students = {}

for _ in range(int(input())):
    name = input()
    score = float(input())
    students[name] = score

total_scores = students.values()
second_low_score = (sorted(list(set(total_scores)))[1])

second_lowest_scores = []
for student_name, student_score in students.items():
    if(student_score == second_low_score):
        second_lowest_scores.append(student_name)

second_lowest_scores.sort()
for name in second_lowest_scores:
    print(name)
