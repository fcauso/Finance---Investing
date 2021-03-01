# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:41:53 2021

@author: EN288JF
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import matplotlib
assets = ['SNOW','MSFT']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2020-1-1')['Adj Close']

pf_data.tail()
#Normalize the data and plot to view performance
(pf_data/pf_data.iloc[0]*100).plot(figsize=(10,5))
#use the log return for efficient portfalio
log_returns = np.log(pf_data/pf_data.shift(1))
log_returns.cov()
#create the variable that will carry our asstes
num_assets = len(assets)
#Now, we must create two random weights
#numpy array will run two random flots
arr = np.random.random(2)
arr[0] + arr[1]
"""
Does not equal one when added
so you must assign a number btw 0 and 1 to the new array called weights
add a line of code that comes afterwars in the loops section we introduce incrementation
weights ends up being an array when you do np.random
"""
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
weights[0] + weights[1]

"""
Expected Portfolio Return
"""
np.sum(weights*log_returns.mean()*250)
"""
Expected Portfolio Variance
"""
np.dot(weights.T, np.dot(log_returns.cov()*250, weights))
"""
Expected Portfoluo Volatility
"""
np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights)))


pfolio_returns = []
pfolio_volatilities = []
for x in range(100):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities
#convert these list into array

"""
create a dataframe with two columns, return and volatilit
"""
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
portfolios.head()
portfolios.tail()
#plot the scatter plot
portfolios.plot(x='Volatility', y='Return', 
                kind='scatter', figsize=(10,6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')












































