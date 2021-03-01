# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:08:00 2020

@author: EN288JF
"""
import quandl
import numpy as np
import pandas as pd
import math
import random
import statsmodels
import pandas_datareader
"""
Pandas: Allow us to organize data in a tabular form and to attach descriptive 
labels to the rows and the columns of the table

"""
#working with Arrays
a = np.array([[0,1,2,3],[4,5,6,7]])
a.shape # will give you the size, 2X4
#access one of the values in the second rpw but 4th value
a[1,3]
#To replace a value

a[1,2] = 8
a[1,2]
a
#vectors
b = np.array([3,5])
#2D Array = Matrix
#1D Array = Vector
b
#Generating Random Numbers
#random.random()  - Generates a random float in the range [0;1)]
number = random.randint(1,6)
print (number)
np.random.randint(1,6,(4,6))
##FINANCE
#panda.series is a single column data
ser = pd.Series(np.random.random(5), name = "Column 01")
ser
ser[2] #will return third wavle
#pandas.dataframe() is many columns
from pandas_datareader import data as wb
SNOW = wb.DataReader('SNOW', data_source='yahoo', start='2020-10-1')
SNOW
SNOW.head()
#adj close price is adjusted for dividends paid to stock owners and other changes such as stock splits
#data will only include only the yradig dats
SNOW.info()
#repeat the same for three different. Create a dictionary and only have the colum 
tickers = ['SNOW','SQ','MSFT','ORCL']
new_data = pd.DataFrame() #object created
for t in tickers:
    new_data[t] = wb.DataReader(t, 
                                data_source='yahoo',
                                start='2020-10-1')['Adj Close']
new_data.tail()
new_data.info()


#USe Alpha Vantage #key:12KY493IT95G4L9M
import os
import requests
from datetime import datetime
import matplotlib.pyplot as plt
tickers_alpha = ['SNOW','SQ']
alpha_data = pd.DataFrame()

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='12KY493IT95G4L9M')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
"""
The library supports giving its results as json dictionaries (default), 
pandas dataframe (if installed) or csv, simply pass the parameter output_format=
'pandas' to change the format of the output
 for all the API calls in the given class.
 """
ts = TimeSeries(key ='12KY493IT95G4L9M', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='SQ', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the Snow stock')
#CRYPTOCURRENCIES
from alpha_vantage.cryptocurrencies import CryptoCurrencies
cc = CryptoCurrencies(key='12KY493IT95G4L9M', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()

"""
To output data to CSV
mydata.to_csv('path')

To input csv
mydata = pd.read_csv('path')
"""
#Input Data 02
mydata_02 = pd.read_csv('\57 Importing Data - Part III\CSV\Python 3 CSV')
mydata_02.head()















