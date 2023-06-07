import json
import config
import pickle

import numpy as np

class CreditCardApproval():
    def __init__(self,ID, CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN,AMT_INCOME_TOTAL, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, DAYS_BIRTH,DAYS_EMPLOYED, FLAG_MOBIL, FLAG_WORK_PHONE, FLAG_PHONE,FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS):
        self.ID=ID
        self.CODE_GENDER=CODE_GENDER
        self.FLAG_OWN_CAR= FLAG_OWN_CAR
        self.FLAG_OWN_REALTY=FLAG_OWN_REALTY
        self.CNT_CHILDREN = CNT_CHILDREN
        self.AMT_INCOME_TOTAL=AMT_INCOME_TOTAL
        self.NAME_INCOME_TYPE="NAME_INCOME_TYPE_"+NAME_INCOME_TYPE
        self.NAME_EDUCATION_TYPE="NAME_EDUCATION_TYPE_"+NAME_EDUCATION_TYPE
        self.NAME_FAMILY_STATUS="NAME_FAMILY_STATUS_"+NAME_FAMILY_STATUS
        self.NAME_HOUSING_TYPE="NAME_HOUSING_TYPE_"+NAME_HOUSING_TYPE
        self.DAYS_BIRTH=DAYS_BIRTH
        self.DAYS_EMPLOYED=DAYS_EMPLOYED
        self.FLAG_MOBIL=FLAG_MOBIL
        self.FLAG_WORK_PHONE=FLAG_WORK_PHONE
        self.FLAG_PHONE=FLAG_PHONE
        self.FLAG_EMAIL=FLAG_EMAIL
        self.OCCUPATION_TYPE="OCCUPATION_TYPE_"+OCCUPATION_TYPE
        self.CNT_FAM_MEMBERS=CNT_FAM_MEMBERS
       
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file)
   
        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file)
    def get_CreditCardApproval(self):
        self.load_model()
        
        
        
        
      
        
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.ID
        test_array[1] = self.json_data["CODE_GENDER"][self.CODE_GENDER]
        test_array[2] = self.json_data["FLAG_OWN_CAR"][self.FLAG_OWN_CAR]
        test_array[3] = self.json_data["FLAG_OWN_REALTY"][self.FLAG_OWN_REALTY]
        test_array[4] = self.CNT_CHILDREN
        
        test_array[5] = self.AMT_INCOME_TOTAL
        NAME_INCOME_TYPE_index = self.json_data["columns"].index(self.NAME_INCOME_TYPE)
        test_array[NAME_INCOME_TYPE_index]=1
        NAME_EDUCATION_TYPE_index=self.json_data["columns"].index(self.NAME_EDUCATION_TYPE)
        test_array[NAME_EDUCATION_TYPE_index]=1
        NAME_FAMILY_STATUS_index=self.json_data["columns"].index(self.NAME_FAMILY_STATUS)
        test_array[NAME_FAMILY_STATUS_index]=1
        NAME_HOUSING_TYPE_index=self.json_data["columns"].index(self.NAME_HOUSING_TYPE)
        test_array[NAME_HOUSING_TYPE_index]=1
        test_array[10] = self.DAYS_BIRTH
        test_array[11] = self.DAYS_EMPLOYED
        test_array[12] = self.FLAG_MOBIL
        test_array[13] = self.FLAG_WORK_PHONE
        test_array[14] = self.FLAG_PHONE
        test_array[15] = self.FLAG_EMAIL
        OCCUPATION_TYPE_index=self.json_data["columns"].index(self.OCCUPATION_TYPE)
        test_array[OCCUPATION_TYPE_index]=1
        test_array[17] = self.CNT_FAM_MEMBERS
        test_array1 = test_array.reshape(1,-1)
        
        CreditCardApproval=self.model.predict(test_array1)[0]
        
        return CreditCardApproval
        
        