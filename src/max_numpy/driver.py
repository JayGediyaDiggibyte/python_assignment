from util import max_of_row_mins
import numpy as np

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(max_of_row_mins(arr))