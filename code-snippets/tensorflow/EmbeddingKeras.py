# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:24:07 2018

@author: amitabh.gunjan
"""
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



#model = Sequential()
#model.add(Embedding(100, 64, input_length=2000))
#model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, return_sequences = True))
#model.add(LSTM(200, dropout=0.2, recurrent_dropout=0.2))
##model.add(Dense(Yall.shape[1], activation='softmax'))
## the model will take as input an integer matrix of size (batch, input_length).
## the largest integer (i.e. word index) in the input should be
## no larger than 999 (vocabulary size).
## now model.output_shape == (None, 10, 64), where None is the batch dimension.
#
#input_array = np.random.randint(100, size=(250, 2000))
#print(input_array)
#model.compile('rmsprop', 'mse')
#output_array = model.predict(input_array)
#print(output_array)
#print(np.shape(output_array))



input_array = np.random.randint(100, size=(250, 2000))
input_y = np.random.randint(7, size = (250))

Y_dumy = pd.get_dummies(input_y)
X_train, X_test, Y_train, Y_test = train_test_split(input_array, Y_dumy,  test_size=0.1, random_state=0)
print(Y_dumy)


model = Sequential()
model.add(Embedding( input_dim = 100, output_dim = 64, input_length=2000))

#model.output_shape == (None, 2000, 64)
model.output_shape

model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, return_sequences =True))
model.add(LSTM(200, dropout=0.2, recurrent_dropout=0.2))

model.add(Dense(Y_dumy.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=5, verbose=True, validation_data=(X_test, Y_test))


#print(input_array)
#model.compile('rmsprop', 'mse')
#output_array = model.predict(input_array)













