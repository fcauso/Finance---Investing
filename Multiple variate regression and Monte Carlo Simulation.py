# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:52:44 2021

@author: EN288JF
"""

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('C:\\Users\\EN288JF\\OneDrive - EY\\Desktop\\Python for Finance\\Housing.xlsx')
X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
#add brackets to show that x is multiple dimensions
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
X2 = data[['House Size (sq.ft.)', 'Year of Construction']]
#add brackets to show that x is multiple dimensions
Y1 = data['House Price']
"""
Monte Carlo
Predict the firms future gross profit
thus, we will need the expected revenue and expected COGS
we will do 1K simulations of the companys revenue
"""
rev_m = 170
rev_stdev = 20
iterations = 1000 #simulations
#produce simulation of future exepected revenue,m we apply numpuys random normal dist
rev = np.random.normal(rev_m, rev_stdev, iterations)
rev
#plot these observations and see their distributions
plt.figure(figsize=(15,6))
plt.plot(rev)
plt.show()
#all fit between 150 and 190. mean -+ stdev
#now lets simulate the cost of goods sold
#assume you know that cogs is 60 % of the rev. and it should deviate 10%
COGS = -(rev*np.random.normal(0.6,0.1))
plt.figure(figsize = (15,6))
plt.plot(rev)
plt.show()
"""
we do not need to simulate cogs. we need to assign a random cogs value
for each of the 1K points. COGS is a % of revenue. mean of 0.6 and a std dev .1
"""
COGS.mean()
COGS.std()
"""
Predicting gross Profit
From the plot we will see that it is norm distributed with mean value
equal to the difference between the mean of the revenues
"""
Gross_Profit = rev + COGS
Gross_Profit
plt.figure(figsize=(15,6))
plt.plot(Gross_Profit)
plt.show()

max(Gross_Profit)
min(Gross_Profit)
#histogram can help you identify the dist of your output
plt.figure(figsize=(10,6));
plt.hist(Gross_Profit, bins = [40,50,60,70,80,90, 100,110,120]);
plt.show()
# bins are chunks in which the data in the plot will be divided
#40 and 50 grouped in one bin btw 50 and 60 grouped in another and so on.
"""
You can also assign the number of bins directly, the computer wil auto split
this allows you to see how it is normally distributed
Allows to predict future cost, gogs, and 
"""
plt.figure(figsize=(15,6));
plt.hist(Gross_Profit, bins = 20);
plt.show()

















