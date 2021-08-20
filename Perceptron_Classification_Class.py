import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Percepton:
    def __init__(self):
        pass

    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        self.number_class = len(np.unique(Y_train))

        lr = 0.001
        self.w = np.random.rand(2, 1)
        self.b = np.random.rand(1, 1)
        Error = []
        for i in range(self.X_train.shape[0]):

            y_pred = np.matmul(self.X_train[i], self.w) + self.b
            e = self.Y_train[i] - y_pred

            self.w += lr * self.X_train[i, :].T * e
            self.b += lr * e

            Y_pred = np.matmul(self.X_train, self.w) + self.b
            error = np.mean(np.abs(self.X_train - Y_pred))
            Error.append(error)

        return Error, self.w, self.b

    def predict(self, X_test):
        Y_pred = np.matmul(X_test, self.w) + self.b
        return Y_pred

    def evaluate(self, data):
        Y_pred = np.matmul(data, self.w) + self.b
        error = np.mean(np.abs(data - Y_pred))
        return error


data1 = pd.read_csv('linear_data_train.csv')
data2 = pd.read_csv('linear_data_test.csv')

X_train = np.matrix(data1.iloc[:, 0:2])
Y_train = np.array(data1.iloc[:, 2])
X_test = np.matrix(data2.iloc[:, 0:2])
Y_test = np.array(data2.iloc[:, 2])

p = Percepton()
Error, w, b = p.fit(X_train, Y_train)
print(Error)
EvalTrain = p.evaluate(X_train)
print('Train Data Evaluation: ', EvalTrain)
EvalTest = p.evaluate(X_test)
print('Test Data Evaluation: ', EvalTest)
