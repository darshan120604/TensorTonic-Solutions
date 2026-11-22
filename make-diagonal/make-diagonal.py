import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    N = len(v)
    arr = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            if i==j:
                arr[i][j] = v[i]

    return arr