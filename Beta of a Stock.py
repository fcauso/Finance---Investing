# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:33:52 2021

@author: EN288JF
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['SNOW','MSFT','^GSPC', '^IXIC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2015-1-1', 
                            end = '2020-12-31')['Adj Close']

data_month = pd.DataFrame().append(data.iloc[0])
for i in range(1, len(data)):
    if data.iloc[[i-1]].index.month != data.iloc[[i]].index.month:
        data_month = data_month.append(data.iloc[i])
# Returns
sec_returns = np.log(data / data.shift(1))
cov = sec_returns.cov()*250
cov
cov_with_market_snow = cov.iloc[0,2]
cov_with_market_snow
#ILOC[] is a method allowing you to access a value from your object
#.ilov[row#, column#] counting starts from 0 not 1
market_var_SP = sec_returns['^GSPC'].var()*250
Snow_beta = cov_with_market_snow / market_var_SP
Snow_beta
market_var_Nasdaq = sec_returns['^IXIC'].var()*250
cov_with_market_MSFT = cov.iloc[1,2]
MSFT_beta = cov_with_market_MSFT / market_var_Nasdaq
MSFT_beta
"""
Sharpe Ratio and
CAPM
"""
MSFT_er = 0.025 + MSFT_beta * .05
SHARPE = (MSFT_er - 0.025) / (sec_returns['MSFT'].std()*250 **.05)
SHARPE
