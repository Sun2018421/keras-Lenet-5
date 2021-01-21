import numpy as np
import keras
from keras.datasets import mnist
from keras.models import load_model

def main():
    model = load_model('Lenet-5.h5')
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    print(type(X_test))
main()