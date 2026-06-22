from src.numpy_liner.util import matrix_determinant
import numpy as np

def test_matrix_determinant_zero():
    matrix = np.array([
        [1.1, 1.1],
        [1.1, 1.1]
    ])
    assert matrix_determinant(matrix) == 0.0

def test_matrix_determinant_negative_three():
    matrix = np.array([
        [1, 2],
        [2, 1]
    ])
    assert matrix_determinant(matrix) == -3.0