from src.numpy_mean.util import calculate_statistics
import numpy as np
import pytest

def test_calculate_statistics():
    arr = np.array([
        [1, 2],
        [3, 4]
    ])
    mean_result, var_result, std_result = calculate_statistics(arr)
    np.testing.assert_array_equal(
        mean_result,
        np.array([1.5, 3.5])
    )
    np.testing.assert_array_equal(
        var_result,
        np.array([1.0, 1.0])
    )
    assert round(std_result, 11) == round(1.11803398875, 11)