import numpy as np
import keras
from keras.datasets import mnist
from keras.models import load_model
from PIL import Image

def showmodel():
    model = load_model('lenet-5(new).h5')
    model.summary()

def readmodel():
    model = load_model('lenet-5(new).h5')
    return model

def showdata():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    x_train = x_train / 255
    x_test = x_test / 255

    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)
    picture_1 = x_test[0:2].reshape(-1,28,28,1)
    label_1 = y_test[0]
    # img = Image.fromarray(picture_1)
    # img.save('test-1.png')
    # print('x_test[0] = ')
    # print(picture_1)
    # print('y_test[0] = ')
    # print(label_1)
    model = readmodel()
    y_pre = model.predict_on_batch(picture_1)
    print(y_pre.shape)

showdata()