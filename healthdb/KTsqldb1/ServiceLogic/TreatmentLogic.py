# Treatment logic

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def getSymptomsList():
    dataframe = pd.read_excel('SymptomsList.xlsx', sheet_name= 'Sheet1')
    # for id in dataframe['ID']:
    #     print("id : ", id)
    # return
    return zip(dataframe['ID'], dataframe['Name'])

