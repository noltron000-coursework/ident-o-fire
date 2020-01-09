import glob
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras
from PIL import Image
from keras.preprocessing.image import img_to_array


input_shape = (128, 128, 3)
print(input_shape)
num_classes = 1
batch_size = 12
epochs = 2


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='sigmoid'))

model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

model.fit_generator(steps_per_epoch=len(df_fire) // batch_size, epochs=epochs, verbose=1, generator=data_gen(df_fire, batch_size=batch_size))
