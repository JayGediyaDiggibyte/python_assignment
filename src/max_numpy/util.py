import numpy as np

def max_of_row_mins(arr):
    return np.max(np.min(arr, axis=1))