import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    trace = 0
    n = len(A)
    for i in range(n):
        trace = trace + A[i][i]

    return trace