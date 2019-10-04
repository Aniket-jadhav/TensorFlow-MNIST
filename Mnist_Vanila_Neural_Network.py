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
