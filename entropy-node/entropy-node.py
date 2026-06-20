import numpy as np

def entropy_node(y):
    l = len(y)
    if l == 0:
        return 0.0
    num_classes = np.unique(y,return_counts=True)
    prop = []
    
    for i in range(len(num_classes[1])):
        prop.append(num_classes[1][i] / l)
    
    entropy = [(i*np.log2(i)) for i in prop]
    return -sum(entropy)