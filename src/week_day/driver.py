from utli import find_day

month, day, year = map(int, input().split())
print(find_day(month, day, year))