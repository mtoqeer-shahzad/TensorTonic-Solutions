import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    try:
        X = np.array(matrix, dtype=float)
    except:
        return None

  
    if X.ndim != 2:
        return None

   
    if axis is not None and axis not in [0, 1]:
        return None

    if norm_type == 'l2':
        norm = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))

    elif norm_type == 'l1':
        norm = np.sum(np.abs(X), axis=axis, keepdims=True)

    elif norm_type == 'max':
        norm = np.max(np.abs(X), axis=axis, keepdims=True)

    else:
        return None

    if axis is None:
        if norm_type == 'l2':
            norm = np.sqrt(np.sum(X ** 2))
        elif norm_type == 'l1':
            norm = np.sum(np.abs(X))
        elif norm_type == 'max':
            norm = np.max(np.abs(X))

    norm = np.where(norm == 0, 1, norm)
    return X / norm  

print(matrix_normalization([[3,4],[1,0]],axis=1))