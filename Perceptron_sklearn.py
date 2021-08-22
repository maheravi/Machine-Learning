from sklearn.linear_model import Perceptron
import pandas as pd
import numpy as np


data1 = pd.read_csv('linear_data_train.csv')

data2 = pd.read_csv('linear_data_test.csv')

X_train = np.array(data1.iloc[:, 0:2])
Y_train = np.array(data1.iloc[:, 2])
X_test = np.array(data2.iloc[:, 0:2])
Y_test = np.array(data2.iloc[:, 2])

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X_train, Y_train)
prediction = clf.predict(X_test)
print(prediction)

print('accuracy: ', clf.score(X_test, Y_test))