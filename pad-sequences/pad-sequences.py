import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.empty((0, max_len or 0), dtype = int)

    L = max_len if max_len is not None else max((len(seq)  for seq in seqs), default = 0)

    ans = np.full((len(seqs), L), pad_value, dtype = int)

    for i,seq in enumerate(seqs):
        trunc = seq[:L]
        ans[i,:len(trunc)] = trunc

    return ans