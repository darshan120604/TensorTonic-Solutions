import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    a = np.asarray(x)
    m = np.mean(a)

    diff = a - m
    sq_diff = diff * diff
    
    # Divide by (n - 1) for sample variance
    variance = np.sum(sq_diff) / (n - 1)
    std_dev = np.sqrt(variance)

    ans = {
        "variance": float(variance),
        "standard_deviation": float(std_dev)
    }
    return ans
