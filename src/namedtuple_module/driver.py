from utli import average_marks

n = int(input())
columns = input().split()
student_data = [input() for _ in range(n)]
result = average_marks(n, columns, student_data)
print(f"{result:.2f}")