def finding_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        total_score = student_marks[query_name]
        avg = sum(total_score) / len(scores)
        print(f"{avg:.2f}")