# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:55:25 2020
USE f9 WHY IDK
@author: EN288JF
"""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
 
SNOW = wb.DataReader('SNOW', data_source='yahoo', start='2020-1-7')
SNOW
SNOW.head()
MSFT = wb.DataReader('MSFT', data_source='yahoo', start='2020-1-7')
MSFT.head()
MSFT.tail()

"""Create a Simple Rate of Return Column"""
#shift allows you do the one before
MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print (MSFT['simple_return'])
MSFT['simple_return'].plot(figsize=(8, 5))
"""
Can create average returns daily with the mean
average returns anually my *250 which is usually the number of trading days in 
a year
"""
avg_returns_d = MSFT['simple_return'].mean()
avg_returns_d
avg_returns_a = MSFT['simple_return'].mean()*250
avg_returns_a
""" Can round it, turn it into a string and make it a % """
print (str(round(avg_returns_a, 4)*100)+'%')
""" Using Log Returns """
MSFT['log_return'] = np.log(MSFT['Adj Close'] / MSFT['Adj Close'].shift(1))
MSFT['log_return'].plot(figsize = (8, 5))
log_return_a = MSFT['log_return'].mean()*250
print(str(round(log_return_a, 4)*100)+ '%')
"""Calculate the Rate of Return of a Portfolio of Securities"""
tickers = ['MSFT', 'CRM', 'GOOGL','ORCL', 'SQ']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start = '2020-1-7')['Adj Close']
mydata.info()
"""Always normalize, here we normalize to 100"""
mydata.iloc[0]
(mydata / mydata.iloc[0] * 100).plot(figsize = (15,6));

mydata.loc['2020-1-6'] #gives the dates as the labels
mydata.iloc[0]
""" Calculate the Return of a Portfolio of Securities """
returns = (mydata / mydata.shift(1)) - 1
weights = np.array([.25,.25,.25,.25])
returns.head()
np.dot(returns,weights)
""" Above gave you a matrix of number because you forgot to calculate the abg return first"""
annual_returns = returns.mean()*250
np.dot(annual_returns, weights)
pfolio_1 = str(round(np.dot(annual_returns, weights),5)*100) + '%'
pfolio_1
weights_2 = np.array([.4,.45,.10,.05])
pfolio_2 = str(round(np.dot(annual_returns,weights_2),4)*100) + '%'
pfolio_2
"""STOCK INDICES  Calculatr the return of this"""
ind_tickers = ['^GSPC', '^IXIC', '^GDAXI']
ind_data = pd.DataFrame()
for t in ind_tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo', start = '2020-1-7')['Adj Close']
ind_data.head()
#lets plot this data in the graph and normalize it
(ind_data / ind_data.iloc[0]*100).plot(figsize=(15,6))
ind_return = (ind_data / ind_data.shift(1)) - 1
annual_ind_return = ind_return.mean()*250
annual_ind_return

"""Calculating the Risk"""
tickers_risk = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers_risk:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start = '2020-1-1')['Adj Close']
sec_data.tail()
#allows us to get the mean and stdev
sec_returns = np.log(sec_data / sec_data.shift(1))
sec_returns
sec_returns['PG'].mean()*250
sec_returns['PG'].std()*250**.5
sec_returns['BEI.DE'].std()*250**.5
""" Can do two tickers at the same time because they are float values.
there cannot be a float with two values. We must create an array with two 
dimensions so we do a double brackets"""
sec_returns[['PG','BEI.DE']].mean()*250 #elements in one matrix and st dev in another





