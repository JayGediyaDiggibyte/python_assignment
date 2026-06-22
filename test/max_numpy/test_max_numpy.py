from src.max_numpy.util import max_of_row_mins
import pytest
import numpy as np

def test_max_of_row_mins_case_1():
    arr = np.array([
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ])
    assert max_of_row_mins(arr) == 3