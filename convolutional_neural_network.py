# -*- coding: utf-8 -*-
"""Convolutional Neural Network

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BKGw5UD9Ch_AOxqXquRfu1aYVCGEH8OX
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras

fashion_mnist= keras.datasets.fashion_mnist
(X_train_full,y_train_full),(X_test,y_test)=fashion_mnist.load_data()

class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

"""# **Data Reshape**"""

X_train_full=X_train_full.reshape(60000,28,28,1)
X_test= X_test.reshape(10000,28,28,1)

"""# Data **Normalization** """

X_train_n= X_train_full/255
X_test_n=X_test/255

X_valid, X_train= X_train_n[:5000],X_train_n[5000:]
y_valid,y_train= y_train_full[:5000],y_train_full[5000:]
X_test=X_test_n

np.random.seed(42)
tf.random.set_seed(42)

model= keras.models.Sequential()
model.add(keras.layers.Conv2D(filters=32,kernel_size=(3,3),strides=1,padding='valid',activation='relu',input_shape=(28,28,1)))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(300,activation='relu'))
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dense(10,activation='softmax'))

model.summary()

model.compile(loss='sparse_categorical_crossentropy',
              optimizer="sgd",
              metrics=["accuracy"])

model_history= model.fit(X_train,y_train,epochs=64,batch_size=64,validation_data=(X_valid,y_valid))

import pandas as pd
pd.DataFrame(model_history.history).plot(figsize=(8,5))
plt.grid(True)
plt.gca().set_ylim(0,1)
plt.show()

ev= model.evaluate(X_test_n,y_test)

ev

X_new=X_test[:3]

y_pred=model.predict_classes(X_new)
y_pred

y_test

print(plt.imshow(X_test[0].reshape((28,28))))