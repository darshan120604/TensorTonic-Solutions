import numpy as np


def euclidean_distance(x: list, y: list) -> float:
    """Returns the Euclidean distance as a Python float."""
    arrx = np.asarray(x)
    arry = np.asarray(y)

    diff = arrx - arry
    squared_diff = diff * diff
    total = np.sum(squared_diff)
    ans = np.sqrt(total)

    return float(ans)
