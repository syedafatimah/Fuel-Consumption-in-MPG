# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 08:23:07 2022

@author: Syeda Fatima Zahid
"""

import pickle
from flask import Flask, request, jsonify
from Model.ml_model import predict_mpg


app = Flask('mpg_prediction')

@app.route('/predict', methods=['POST'])
def predict():
    vehicle = request.get_json()
    print(vehicle)
    with open('./Model/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_mpg(vehicle, model)

    result = {
        'mpg_prediction': list(predictions)
    }
    return jsonify(result)

@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model!!"