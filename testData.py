import numpy as np
import keras
from keras.datasets import mnist
from keras.models import load_model

def main():
    model = load_model('lenet-5(new).h5')
    model.summary()

main()