from util import matrix_determinant
import numpy as np

n = int(input())
matrix = np.array(
    [list(map(float, input().split())) for _ in range(n)]
)
print(matrix_determinant(matrix))