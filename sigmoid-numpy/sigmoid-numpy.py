import numpy as np

def sigmoid(x):
    x = np.array(x)
    d = 1 + np.exp(-x)
    return 1 / d