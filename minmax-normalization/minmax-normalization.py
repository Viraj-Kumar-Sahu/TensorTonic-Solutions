import numpy as np

def minmax_scale(X, axis, eps=1e-12):
    X = np.array(X, dtype=float)

    mn = np.min(X, axis=axis, keepdims=True)
    mx = np.max(X, axis=axis, keepdims=True)

    return (X - mn) / (mx - mn + eps)