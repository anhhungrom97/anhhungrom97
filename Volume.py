# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:38:12 2022

@author: HOANG
"""

import investpy
import pandas as pd
import datetime as dt

from sklearn.preprocessing import MinMaxScaler

import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

import matplotlib.pyplot as plt
# Load data
start = '01/01/2022'
end = dt.datetime.now().strftime("%d/%m/%Y")

dfmack=pd.read_csv("C:\\Users\\HOANG\\Desktop\\Python\\Ma CK Viet Nam1.csv")
dfmack=pd.DataFrame(dfmack)
dfmack=dfmack.loc[dfmack['SAN']=='HNX']
listck=dfmack['Ma CK'].values.tolist()
#search_result = investpy.get_stocks_list(country='VietNam')
print(listck)
dates = pd.date_range(start, end)
 
df = pd.DataFrame(index = dates)
company = listck
for lck in listck:
    company = lck
    f = investpy.get_stock_historical_data(stock=company, country='VietNam', from_date=start, to_date=end)
    
    f=pd.DataFrame(f['Volume'])
    
    f = f.rename(columns = {"Volume" : lck})

    print(f)
    df = df.join(f)
    
df.head()
df=df.dropna()
df.to_csv("C:\\Users\\HOANG\\Desktop\\Python\\Volume.csv")