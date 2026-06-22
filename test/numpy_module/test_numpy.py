from src.numpy_module.util import floor_ceil_rint
import numpy as np
import pytest

def test_floor_ceil_rint():

    floor_arr, ceil_arr, rint_arr = floor_ceil_rint(
        ["1.1", "2.2", "3.3", "4.4", "5.5", "6.6", "7.7", "8.8", "9.9"]
    )

    np.testing.assert_array_equal(
        floor_arr,
        np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
    )

    np.testing.assert_array_equal(
        ceil_arr,
        np.array([2., 3., 4., 5., 6., 7., 8., 9., 10.])
    )

    np.testing.assert_array_equal(
        rint_arr,
        np.array([1., 2., 3., 4., 6., 7., 8., 9., 10.])
    )