import numpy as np

def leaky_relu(x, alpha=0.01):
    x = np.array(x)
    return np.where(x < 0, alpha*x, x)