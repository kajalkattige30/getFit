from subprocess import call
import numpy as np
from flask import Flask, request, jsonify, render_template
import json
#import pickle

app = Flask(__name__)

#model2 = pickle.load(open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/myfile2.pkl",'rb'))




class CallPy(object):

    def __init__(self, path = 'models/be_proj_ml_algo.py'):
        self.path = path
    
    def call_algo(self):
        call(["Python3", "{}".format(self.path)])
    

@app.route('/')
def home():
    return "Flask server"


@app.route('/nodeFlask', methods = ['POST'])
def meal_predict():
    #data = request.get_json()
    #print(data)
    # we are getting this data from node server, now pass this data to ml algorithm
    # with open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/dic.json") as f1:
    #     macros = json.load(f1)

    with open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/meal.json") as f2:
        meals = json.load(f2)
    
    out_file = open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json", "w") 
    json.dump(meals, out_file, indent = 2)
    out_file.close() 
    return meals
    #return json.dumps("new data" : "Ml algorithm output")

meal_predict()



if __name__ == "__main__":
    c = CallPy()
    c.call_algo()
    app.run(debug=True)