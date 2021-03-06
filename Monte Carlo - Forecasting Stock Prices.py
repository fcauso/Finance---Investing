# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:59:32 2021

@author: EN288JF
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo',
                             start = '2007-1-1')['Adj Close']
log_returns = np.log(1 + data.pct_change())
"""
pandas.pct_change()
this syntax is used to obtain simple returns from a provided dataset
"""
log_returns.tail()
data.plot(figsize = (16,5))
#now the logs of returns plot to view distribution
log_returns.plot(figsize = (16,6))
#returns are normally distributed and have a normal mean
"""
Now we need the mean and variance to calculate the drift
mean - half of the variance
give an expectation of logs
"""
u = log_returns.mean()
var = log_returns.var()
Drift = u - (0.5*var)
Drift
stdev = log_returns.std()
stdev
"""
Brownian Motion:
    r = drift+stdev*e^r
"""
type(Drift)
type(stdev)
"""
use the numpy array formula to change valuues to an  array
however
you can also do object.values
this transfers the object into a numpy array
"""
Drift.values
np.array(Drift)
stdev.values 
"""
Z corresponds to the distance btw the mean and the events, 
expressed as the number of standard deviations
"""
norm.ppf(0.95)
x = np.random.rand(10,2) # we need two values to make a multi dimensionsla
norm.ppf(x)
"""
After you create a random variable and do the norm.ppf()
you can see that the first number from the first row corresponds to the first
probability from the first row of the X matrix
"""
z = norm.ppf(np.random.rand(10,2))

"""
The newly created Z array use the probabilities generated by the random variable
amd converted them into distances from the mean zeroas mesured by st dev.
this expression will create the value Z as defined in our formula
"""
t_intervals = 1000 # forecasting the stock price for the upcoming 1000 days
iterations = 10 # this gives ten series of future stock predictions
"""
daily_returns = e^r
r = drift + stdev*z
"""
daily_returns = np.exp(Drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, 
                                                                             iterations)))
daily_returns
# this should give us 10 columns 1000 rows
"""
Next step is to create a price list
Each price must be equal to the product of the price observed in the previous day and the simulated
daily return.
If we determin the price and date, we can estimate the expected stock price we will have in a day plus one
"""
s0 = data.iloc[-1]
s0
#this is the first stock price of our list
 """
 np.zeros_like()
 this provides us with an array with the same dimensions as an array that existed before
 """
price_list = np.zeros_like(daily_returns)
price_list 
#this object was created so that we can replace these zeros with stock prices using a loop
#first we must set our first row to s0 
price_list[0] = s0
price_list[0]
#we write down the formula for the expected stock price on date t equal to the price in day t minus one ti,me
#we must set up a loop that begins on day 1 and ends at day 1000
for t in range(1, t_intervals):
    price_list[t] = price_list[t-1] * daily_returns[t]

price_list 
plt.figure(figsize = (16,4))
plt.plot(price_list)
























