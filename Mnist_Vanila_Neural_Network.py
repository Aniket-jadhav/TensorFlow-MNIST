#Run this program on google colab, so that you don't have to install the libraries on local machine.

## 1. Import Libraries
from __future__ import absolute_import, division, print_function
import tensorflow as tf
import matplotlib.pyplot as plt
import keras

## 2. Load the dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

## 3. Check the dimentions of the dataset
train_images.shape

## 4. Grayscale to binary
x_train, x_test = x_train / 255.0, x_test / 255.0

## 5. Plot some input
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(y_train[i])
plt.show()
