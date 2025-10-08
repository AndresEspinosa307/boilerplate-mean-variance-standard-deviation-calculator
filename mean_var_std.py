import numpy as np

def calculate(list):
     if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape((3, 3))
    axis0 = 0  # columns
    axis1 = 1  # rows
    mean = [arr.mean(axis=axis0).tolist(), arr.mean(axis=axis1).tolist(), arr.mean()]
    variance = [arr.var(axis=axis0).tolist(), arr.var(axis=axis1).tolist(), arr.var()]
    standard_deviation = [arr.std(axis=axis0).tolist(), arr.std(axis=axis1).tolist(), arr.std()]
    max_val = [arr.max(axis=axis0).tolist(), arr.max(axis=axis1).tolist(), arr.max()]
    min_val = [arr.min(axis=axis0).tolist(), arr.min(axis=axis1).tolist(), arr.min()]
    sum_val = [arr.sum(axis=axis0).tolist(), arr.sum(axis=axis1).tolist(), arr.sum()]
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    return calculations
