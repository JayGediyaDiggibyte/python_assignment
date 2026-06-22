from util import calculate_statistics
import numpy as np

n, m = map(int, input().split())
arr = np.array(
    [list(map(int, input().split())) for _ in range(n)]
)
mean_result, var_result, std_result = calculate_statistics(arr)
print(mean_result)
print(var_result)
print(std_result)