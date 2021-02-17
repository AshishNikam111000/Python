import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.datasets import imdb
from tensorflow.python.keras.backend import relu
import os
np.set_printoptions(suppress=True)

data = keras.datasets.imdb                                                                  #loading dataset

(traini, trainl), (testi, testl) = data.load_data(num_words=10000)                          #splitting the dataset into train set and test set  (returns numpy array)

word_index = data.get_word_index()
word_index = {k:(v+3) for k, v in word_index.items()}                                      #mapping the words with the integer array to figure out what it means
word_index["<PAD>"] = 0                                                                    #basically creating out own dict 
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

traini = keras.preprocessing.sequence.pad_sequences(traini, value=word_index["<PAD>"], padding="post", maxlen=250)
testi = keras.preprocessing.sequence.pad_sequences(testi, value=word_index["<PAD>"], padding="post", maxlen=250)

def decode_review(text):                                                                           #decoding all the testing and training data into human readable form
    return " ".join([reverse_word_index.get(i, "?") for i in text])

#creating neural layers/ model
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))                                                       #model.add() - it adds the layer. Same thing as before 
model.add(keras.layers.GlobalAveragePooling1D())                                                   #            but instead of writting it in list we use this funtion.
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

os.system('cls')
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

#creating validation data and train data
x_val = traini[:10000]
x_train = traini[10000:]

y_val = trainl[:10000]
y_train = trainl[10000:]

fit_model = model.fit(x_train, y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val), verbose=1)
results = model.evaluate(testi, testl)
os.system('cls')
print("Tested accuracy: ", results)

for i in range(5):
    temp = testi[i]
    predict = model.predict([temp])
    # print("Review: ", decode_review(temp))
    print("Prediction: "+ str(predict[i]))
    print("Actual: "+ str(testl[i]))

# #saving the model
# model.save("test.h5")

#To use the saved model on our custom text
'''
def review_encode(s):
    encoded = [1]
    for word in s:
        if word in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded

model = keras.models.load_model("model.h5")

with open("test.txt", encoding="utf-8") as f:
    for line in f.readlines():
        nline = line.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace(":", "").replace("\"", "").strip().split(" ")
        encode = review_encode(nline)
        encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post", maxlen=250)
        predict = model.predict(encode)
        print(line, encode, predict[0], sep='\n')
'''

##### Note: Prediction problems because it need numpy version=1.16.1
