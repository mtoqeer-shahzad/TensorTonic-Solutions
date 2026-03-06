import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    return np.array(A).T


print(matrix_transpose([[1,2,3],[3,4,7]]))

