import numpy as np

def gini_impurity(y_left, y_right):
    l1 = len(y_left)
    l2 = len(y_right)

    if l1 == 0 and l2 == 0:
        return 0.0

    _, counts1 = np.unique(y_left, return_counts=True)
    _, counts2 = np.unique(y_right, return_counts=True)

    p1 = counts1 / l1
    p2 = counts2 / l2

    giniL = 1 - np.sum(p1 ** 2)
    giniR = 1 - np.sum(p2 ** 2)

    return (l1 * giniL + l2 * giniR) / (l1 + l2)