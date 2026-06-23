from util import calculate_happiness

n, m = map(int, input().split())
arr = list(map(int, input().split()))
liked = set(map(int, input().split()))
disliked = set(map(int, input().split()))
print(calculate_happiness(arr, liked, disliked))