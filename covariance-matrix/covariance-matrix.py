import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Step 0: Input validation
    X = np.array(X, dtype=float)

    # Invalid input check
    if X.ndim != 2:
        return None
    
    N, D = X.shape
    
    if N < 2:
        return None

    # Step 1: Center the data (mean subtract)
    mean = np.mean(X, axis=0)        # shape (D,)
    X_centered = X - mean            # shape (N, D)

    # Step 2: Covariance matrix
    return (X_centered.T @ X_centered) / (N - 1)