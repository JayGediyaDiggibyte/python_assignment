import numpy as np

def floor_ceil_rint(values):
    arr = np.array(values, float)
    return (
        np.floor(arr),
        np.ceil(arr),
        np.rint(arr)
    )