import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    xa = np.asarray(x)
    pa = np.asarray(p)

    wsum = xa*pa
    ans = np.sum(wsum)

    return float(ans)