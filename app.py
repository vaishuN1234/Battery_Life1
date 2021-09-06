from flask import Flask, render_template,request

import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Basic_Classifier.sav', 'rb'))
model1 = pickle.load(open('High_Regression_Log_Life.sav', 'rb'))
model2 = pickle.load(open('Low_Regression.sav', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        charge_tym	=float(request.form['charge_tym'])
        log10_Var100_10	=float(request.form['log10_Var100_10'])
        Intergration	=float(request.form['Intergration'])
        min1=float(request.form['min1'])
        Dis_max	=float(request.form['Dis_max'])
        Slope	=float(request.form['Slope'])
        Intercept	=float(request.form['Intercept'])
        iR_min	=float(request.form['IR_min'])
        iR_diff	=float(request.form['IR_diff'])
        prediction=model.predict([[min1,charge_tym,log10_Var100_10,Intergration]])
        if prediction==1:
            prediction1=model1.predict([[min1,log10_Var100_10,Dis_max,Slope, Intercept,Intergration,charge_tym,iR_min,iR_diff]])
            output1=prediction1    
            return render_template('index.html',prediction_text="life cycle is High {}".format(output1))
        else:
            prediction2=model2.predict([[min1,log10_Var100_10,Dis_max,Slope, Intercept,Intergration,charge_tym,iR_min,iR_diff]])
            output2=prediction2
            return render_template('index.html',prediction_text="life cycle is Low {}".format(output2))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

