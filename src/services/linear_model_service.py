import csv
import random
import math
import numpy as np

def loadDataset(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        headers = dataset[0]
        dataset = dataset[1: len(dataset)]
        return dataset, headers

def train_test_split(X, Y, split):

    #randomly assigning split% rows to training set and rest to test set
    indices = np.array(range(len(X)))
    
    train_size = round(split * len(X))

    random.shuffle(indices)

    train_indices = indices[0:train_size]
    test_indices = indices[train_size:len(X)]

    X_train = X[train_indices, :]
    X_test = X[test_indices, :]
    Y_train = Y[train_indices, :]
    Y_test = Y[test_indices, :]
    
    return X_train,Y_train, X_test, Y_test


def normal_equation(X, Y):
    beta = np.dot((np.linalg.inv(np.dot(X.T,X))), np.dot(X.T,Y))

    return beta

def predict(X_test, beta):
    return np.dot(X_test, beta)

def predict_value(x0, x1, x2):
    dataset, headers = loadDataset('example.csv')

    dataset = np.array(dataset)
    dataset = dataset.astype(float)

    X = dataset[:, 1:4]      
    Y = dataset[:, -1]   

    #adding ones to X
    one = np.ones((len(X),1))
    X = np.append(one, X, axis=1)
    #reshape Y to a column vector
    Y = np.array(Y).reshape((len(Y),1))

    split = 0.7
    X_train, Y_train, X_test, Y_test = train_test_split(X, Y, split)

    beta = normal_equation(X_train, Y_train)

    values = [1, x0, x1, x2]
    values = np.array(values).reshape((1, len(values)))

    predicted_value = predict(values, beta)

    return predicted_value[0, 0]