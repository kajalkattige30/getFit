from subprocess import call
import numpy as np
import sys
import subprocess
from flask import Flask, request, jsonify, render_template
import json
#import pickle

app = Flask(__name__)

#model2 = pickle.load(open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/myfile2.pkl",'rb'))




class CallPy(object):

    def __init__(self, path = 'C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/models/be_proj_ml_algo.py'):
        self.path = path
    
    def call_algo(self):
        call(["Python3", "{}".format(self.path)])

    

@app.route('/')
def home():
    return "Flask server"


@app.route('/nodeFlask', methods = ['POST'])
def meal_predict():

    # call(["Python3", "{}".format('C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/models/be_proj_ml_algo.py')])
    s2_out = subprocess.check_output([sys.executable, "C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/models/be_proj_ml_algo.py"])

    
    with open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/meal.json") as f2:
        meals = json.load(f2)
    
    out_file = open("C:/Users/kkatt/Documents/BE_Project/getFit/SERVER/api/recommendation.json", "w") 
    json.dump(meals, out_file, indent = 2)
    out_file.close() 
    print("printing s2:",s2_out)
    return "Returning meal recommendation"

    #return json.dumps("new data" : "Ml algorithm output")

#meal_predict()



if __name__ == "__main__":
    c = CallPy()
    c.call_algo()
    app.run(debug=True)