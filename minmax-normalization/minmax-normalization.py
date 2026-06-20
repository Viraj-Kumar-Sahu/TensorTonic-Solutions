import numpy as np

def minmax_scale(X, axis, eps=1e-12):
    x = np.array(X,dtype=float)
    mini = np.min(x,axis=axis,keepdims=True)
    maxi = np.max(x,axis=axis,keepdims=True)

    return ((x - mini) / (maxi - mini + eps))