import keras
from keras.datasets import mnist
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import keras.utils as image

from PIL import Image

import numpy as np


class RecognizeDigit:
    def __init__(self):
        self.train()
    
    def train(self):       
        (train_x,train_y), (test_x,test_y) = mnist.load_data()

        #train_x = train_x.astype('float32') / 255
        #test_x = test_x.astype('float32') / 255


        '''print(train_x)
        print(train_y.shape)
        print(test_x.shape)
        print(test_y.shape)'''


        train_x = train_x.reshape(60000,784)
        test_x = test_x.reshape(10000,784)


        train_y = keras.utils.to_categorical(train_y,10)
        test_y = keras.utils.to_categorical(test_y,10)


        #Initialize our data ************

        self.model = Sequential()
        self.model.add(Dense(units=128,activation="relu",input_shape=(784,)))
        self.model.add(Dense(units=128,activation="relu"))
        self.model.add(Dense(units=128,activation="relu"))
        self.model.add(Dense(units=10,activation="softmax"))


        #*** Compile the model **********


        self.model.compile(optimizer=SGD(0.001),loss="categorical_crossentropy",metrics=["accuracy"])


        self.model.fit(train_x,train_y,batch_size=32,epochs=10,verbose=1)


        #model.save("mnist-model.h5")

        # load feautures after training our model
        self.model.load_weights("mnist-model.h5")
        

    def recognize(self, image_path):
        self.image = Image.open(image_path)
        self.image = self.image.convert('L')
        self.image = self.image.resize((28,28))
        self.image = np.array(self.image)
        self.image = self.image.reshape(1,784)
        #self.image = 255 - self.image
        self.image[self.image<100] = 0
        self.image[self.image>=100] = 255
        self.image = self.image.astype('float32') / 255
        self.predict_x = self.model.predict(self.image)
        self.class_x= np.argmax(self.predict_x, axis = 1)
        self.class_name = self.class_x[0]
        #a = xác suất của các số từ 0-9
        return self.predict_x
    
        