import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.array(A, dtype=float)
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
A = np.array([[1, 2],
              [3, 4]])
inv = matrix_inverse(A)
print(inv)

