import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.python.keras.backend import relu
import os

data = keras.datasets.fashion_mnist                                                         #loading dataset

(traini, trainl), (testi, testl) = data.load_data()                                         #splitting the dataset into train set and test set  (returns numpy array)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',             #labels of the datasets
                'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
   
traini = traini/255.0                                                                       #scaling dataset values in between 0-1
testi = testi/255.0                                                                         #scaling dataset values in between 0-1

model = keras.Sequential([                                                                  #creating neural layers
    keras.layers.Flatten(input_shape=(28,28)),                                              #1st neural layers
    keras.layers.Dense(128, activation="relu"),                                             #hidden neural layers
    keras.layers.Dense(10, activation="softmax")                                            #last/output neural layers
])

os.system('cls')

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(traini, trainl, epochs=5)

# test_loss , test_acc = model.evaluate(testi, testl)
# print("Tested accuracy: ", test_acc)

pred = model.predict(testi)                                                                 #model.predict() return an array having values of the output neurons
# maxindex = np.argmax(pred[7])                                                               #np.argmax() return index of element having highest value
# print(class_names[maxindex])

# for i in range(10):
#     plt.grid(False)
#     plt.imshow(testi[i], cmap=plt.cm.binary)
#     plt.xlabel("Actual: " + class_names[testl[i]])
#     plt.title(("Prediction" + class_names[np.argmax(pred[i])]))
#     plt.show()
