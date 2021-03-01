# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:16:55 2021

@author: EN288JF
"""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

"""
We will create the Black Scholes Formula
S-stiock price
K-Strike price
T-time horizon 9years)
Only difference is that in d1 we add the variance and in d2 we subtract
"""
def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2/2)*T) / (stdev*np.sqrt(T))
"""
We will need the cumulative dist function since it shows how the data
accumulates over time it can never be below 0 or above one
we use norm.cdf will take as an argument a value from the data and will
show us what portion of the data lies below that value.

An argument of zero will give us 0.5 since 0 is the mean of a std normal dist
and half of the data lies below this value.
"""
norm.cdf(0)
norm.cdf(.25)
#now we write the black scholes formula
def BSM(S, K, r, stdev, T):
    return( S * norm.cdf(d1(S, K, r, stdev, T)))-(K*np.exp(-r*T)*norm.cdf(d2(S, K, r, stdev, T)))

"""
N(d1)
norm.cdf(d1(S, K, r, stdev, T))
"""
ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2017-3-21')['Adj Close']

S = data.iloc[-1]
S
"""
.iloc[]
rememeber that gives you the index tjus the last market price
.pct_change
this code gives the percent change over given number of periods
integers is default
"""
log_returns = np.log(1 + data.pct_change())
stdev = log_returns.std()*250**0.5
stdev 
#Now we use a risk free rate, strike price is 110 and year is one
r = 0.025
K = 110.0
T = 1
 
d1(S, K, r, stdev, T)
d2(S, K, r, stdev, T)
BSM(S, K, r, stdev, T)
 


















