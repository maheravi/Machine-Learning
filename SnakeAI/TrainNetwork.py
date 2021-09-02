import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

data = pd.read_csv('DataSetSnake.csv')

y_train = data[['direction']]
x_train = data.drop(columns=['direction'])

X_train, X_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=33)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_val = np.array(X_val)
y_val = np.array(y_val)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax'),
])

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

output = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100)

model.save('save.h5')