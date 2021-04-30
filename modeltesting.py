from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf

import os
model = tf.keras.models.load_model('models/model.h5', compile=False)
print(os.getcwd())

image = plt.imread('static/img/neg1.jfif')
plt.subplot(2, 1, 1)
plt.imshow(image)

simple_pred_classes = ['Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Healthy',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Healthy',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy']

image1 = cv2.resize(image, (64, 64))
plt.subplot(2, 1, 2)
plt.imshow(image1)
#print(image1.shape)
plt.show()

#print(image.shape)
#layer1 = model.layers[0]
#print(layer1.input_shape)
image1 = np.reshape(image1, (1, 64, 64, 3))
prediction = model.predict(image1)

print(prediction)