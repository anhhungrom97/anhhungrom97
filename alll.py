# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:30:46 2022

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
start = '1/5/2022'
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
df.to_csv("C:\\Users\\HOANG\\Desktop\\Python "f"Volume.csv")
df['H-L'] = df['High'] - df['Low']
df['O-C'] = df['Open'] - df['Close']
ma_1 = 7
ma_2 = 14
ma_3 = 21
df[f'SMA_{ma_1}'] = df['Close'].rolling(window=ma_1).mean()
df[f'SMA_{ma_2}'] = df['Close'].rolling(window=ma_2).mean()
df[f'SMA_{ma_3}'] = df['Close'].rolling(window=ma_3).mean()

df[f'SD_{ma_1}'] = df['Close'].rolling(window=ma_1).std()
df[f'SD_{ma_3}'] = df['Close'].rolling(window=ma_3).std()
df.dropna(inplace=True)

#df.to_csv("C:\\Users\\HOANG\\Desktop\\Python "f"{company}.csv")
print("Done Loading Data")
# Process Data

y1=df['H-L']

plt.plot(y1, color="red", label=f"High-Low")
#plt.plot(df['O-C'], color="blue", label=f"Open-Close")
plt.title(f"{company} Prices")
plt.xlabel("Date")
plt.ylabel("Stock Prices")
plt.ylim(bottom=0)
plt.legend()
plt.show()

# Make Prediction



