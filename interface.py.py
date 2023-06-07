from flask import Flask,request,jsonify
import numpy as np

import config
from Credit_API.utils import CreditCardApproval


app = Flask(__name__)
@app.route('/post', methods =['GET', 'POST'])
def post():
    return ('This is the response.html')
@app.route("/Approval",methods = ["POST","GET"])
def get_CreditCardApproval():
    data = request.form
    # print("user input data is",data)

    ID=int(data["ID"])
    CODE_GENDER=data["CODE_GENDER"]
    FLAG_OWN_CAR =data["FLAG_OWN_CAR"]
    FLAG_OWN_REALTY =data["FLAG_OWN_REALTY"]
    CNT_CHILDREN = int(data["CNT_CHILDREN"])
    AMT_INCOME_TOTAL =eval(data["AMT_INCOME_TOTAL"])
    NAME_INCOME_TYPE =data["NAME_INCOME_TYPE"]
    NAME_EDUCATION_TYPE =data["NAME_EDUCATION_TYPE"]
    NAME_FAMILY_STATUS =data["NAME_FAMILY_STATUS"]
    NAME_HOUSING_TYPE =data["NAME_HOUSING_TYPE"]
    DAYS_BIRTH =eval(data["DAYS_BIRTH"])
    DAYS_EMPLOYED =eval(data["DAYS_EMPLOYED"])
    FLAG_MOBIL =int(data["FLAG_MOBIL"])
    FLAG_WORK_PHONE =int(data["FLAG_WORK_PHONE"])
    FLAG_PHONE =int(data["FLAG_PHONE"])
    FLAG_EMAIL =int(data["FLAG_EMAIL"])
    OCCUPATION_TYPE =data["OCCUPATION_TYPE"]
    CNT_FAM_MEMBERS =eval(data["CNT_FAM_MEMBERS"])
    Approval= CreditCardApproval(ID, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN,
       AMT_INCOME_TOTAL, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE,
       NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, DAYS_BIRTH,
       DAYS_EMPLOYED, FLAG_MOBIL, FLAG_WORK_PHONE, FLAG_PHONE,
       FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS)
    Prediction = Approval.get_CreditCardApproval()
    
    # if Prediction == 0 :
    # return ('This is the test program.html')
    # return jsonify({"Result": Prediction})


    # else:
    return jsonify({"Result":f"Credit Card Approval Prediction is Decline{Prediction}"})


if __name__ =="__main__":
    # app.debug = True
    # app.run()
    app.run()
    # host = 'localhost', port = 8088, debug = True

