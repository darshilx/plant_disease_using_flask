from flask import Flask, redirect, render_template, request, jsonify, json
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2
import matplotlib.pyplot as plt
import os
from load import *
import sys
import re
import io
from werkzeug.utils import secure_filename
import tensorflow as tf
from keras.models import load_model

app = Flask(__name__)
app.static_folder = 'static'

UPLOAD_FOLDER = "uploads"


model = tf.keras.models.load_model('models/model.h5', compile=False)


#def load_and_preprocess_image(path):
 #   img = tf.io.read_file(path)

def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    show_img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32')
    x /= 255
    preds = model.predict(x)
    return preds

@app.route('/')
def index():
    print("Hello")
    return render_template('index.html')


@app.route('/predict', methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        file = request.files["img"]
        upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(upload_image_path)

        preds = model_predict(upload_image_path, model)
        print(preds[0])

        # x = x.reshape([64, 64]);
        disease_class = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
                         'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
                         'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                         'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
                         'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
        a = preds[0]
        ind = np.argmax(a)
        print('Prediction:', disease_class[ind])
        result = disease_class[ind]
        return result
    return "Uploaded"


if __name__ == "__main__":
    app.run(debug=True, port=8000)