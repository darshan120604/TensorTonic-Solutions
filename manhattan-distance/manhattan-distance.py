import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    ans = 0.0
    n = len(x)
    for i in range(n):
        curr = 0
        curr = x[i] - y[i]
        if curr < 0:
            curr = curr * -1
       

        ans = ans + curr
        
    return ans