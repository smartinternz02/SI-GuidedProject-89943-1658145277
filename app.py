# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:06:54 2022

@author: kvssn
"""

import numpy as np

import pickle

from flask import Flask, request, render_template

app=Flask(__name__)
model = pickle.load(open(r"C:\Users\kvssn\OneDrive\Desktop\demo\model3.pkl",'rb'))

@app.route('/', methods=['GET'])

def index():

    return render_template("sample.html")

@app.route('/sample.html', methods=['GET'])
def about():
    return render_template("sample.html")
@app.route('/sample2', methods=['GET'])
def page():
    return render_template("sample2.html")

@app.route('/sample3', methods=['GET', 'POST'])
def predict():

    input_features = [float(x) for x in request.form.values()] 
    features_value = [np.array(input_features)]

    print(features_value)

    #features_name = ['city', 'BHKS', 'sqft_per_inch', 'build_up_area", "Type_of_property', 'deposit']

    prediction =model.predict(features_value)

    output=prediction[0] #np.exp(predictions)

    output = np.exp(output)

    output= np.round(output)

    print(output)

    return render_template(r"sample2.html", prediction_text= 'House Rent is {}' .format((output)))

if __name__=='__main__':

    app.run(debug=False)
