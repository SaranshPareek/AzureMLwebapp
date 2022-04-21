import numpy as np
from flask import Flask, request, jsonify, render_template
import urllib.request
import json
import os
import ssl


app = Flask(__name__)

from req11 import req_model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    input_ = [int_features]
    prediction = req_model(dat = input_)


    return render_template('index.html', prediction_text = {"message" : prediction[0], "result" : prediction[1]})


if __name__ == "__main__":
    app.run(debug=True)