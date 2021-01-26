import keras
from keras.datasets import mnist
from keras.models import load_model

def Getdata():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

    x_train = x_train / 255
    x_test = x_test / 255

    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)

    data = x_test[0].reshape(-1)
    ans = y_test[0]
    for i in range(28):
        for j in range(28):
            print("%.6f , " % data[i*28+j],end='')
        print('')
    print(ans)
Getdata()