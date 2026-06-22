import numpy as np

def calculate_statistics(arr):
    mean_result = np.mean(arr, axis=1)
    var_result = np.var(arr, axis=0)
    std_result = np.std(arr)
    return mean_result, var_result, std_result