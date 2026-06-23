from util import word_order

n = int(input())
words = [input() for _ in range(n)]
distinct_count, occurrences = word_order(words)
print(distinct_count)
print(*occurrences)