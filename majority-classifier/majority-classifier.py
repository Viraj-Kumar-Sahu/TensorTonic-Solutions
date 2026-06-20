import numpy as np

def majority_classifier(y_train, X_test):
    num_classes = np.unique(y_train,return_counts=True)
    idx = num_classes[1].argmax()
    return np.full(len(X_test),num_classes[0][idx])