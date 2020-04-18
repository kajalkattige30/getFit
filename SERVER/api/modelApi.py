import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model2 = pickle.load(open("C:/Users/Janhavi Dubule/Desktop/BE Project/getFit/SERVER/myfile1.pkl",'rb'))

@app.route('/')
def home():
    return ('nodeFlask.js')

@app.route('/nodeFlask', methods = ['POST'])
def meal_predict():
    data = request.get_json()
    print(data)
    prediction = model2.meal_predict(data)
    return render_template('nodeFlask.js', prediction_text = 'Meal recommendations are : {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)