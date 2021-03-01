# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:35:25 2021

@author: EN288JF
"""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = '2007-1-1')['Adj Close']

log_returns = np.log(1 + data.pct_change()) 
"""
Euler
the stock price today equals the stock price yesterday  times e to the power of the risk free rate
minus half the variance of the log returns multiplied by a fixed time interval delta t plus the standard
deviation multiplied by the square root of delta t times a random component Z
"""
r = 0.025
stdev = log_returns.std()*250**0.5
stdev
type(stdev)

stdev = stdev.values
stdev
T = 1.0 #forecasting prices for one year ahead
t_intervals = 250 #number of trading days in a given year
delta_t = T / t_intervals #fixed time interval component
iterations = 10000 #how many times we want to simulate the random component Z

"""
The random component Z will be a matrix with random components as drawn from
a standard normal distribution with mean 0 and stdev of one.

The dimension of the matrix these values will occupy will be defined by the number of time intervals
augmented by on ein the number of iteration 
"""

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0
S0 

"""
We loop from one to the number of time intervals plus one and we create a whole stock price matrix with
the dimension of the time intervals plus one to the number of iterations
more precisely hundred and plus one equals 251 and we have ten thousand iterations.
So the dimension of this matrix is 251 to ten thousand to plot only ten simulations
"""
for t in range(1, t_intervals + 1):
    S[t] = S[t-1]*np.exp((r - 0.5*stdev**2) * delta_t + stdev*delta_t**0.5*Z[t])
S
S.shape #this gives the dimensions of the matrix
#now we only want to plot 10
plt.figure(figsize = (16,6))
plt.plot(S[:, :10]); #first colon signifies all 251 rows, then next limits the grph to the first 10 iterations

"""
Call Option:
    S-K>0 you buy
    S-K<0 don't buy
We will use a numpy array called
numpy.maximum() which will create an array that contains either 0s or the numbers
equal to the differences
"""
p = np.maximum(S[-1] - 110, 0)

p.shape

C = np.exp(-r * T) * np.sum(p) / iterations
C


















