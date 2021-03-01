# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:58:16 2021
Linear Regression

@author: EN288JF
"""

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data_housing = pd.read_excel('C:\\Users\\EN288JF\\OneDrive - EY\\Desktop\\Python for Finance\\Housing.xlsx')
data_housing
data_housing.head()


data_housing.head()
data_housing[['House Price', 'House Size (sq.ft.)']]
X_Explanatory=data_housing['House Size (sq.ft.)']
Y_Dependent=data_housing['House Price'] 
X_Explanatory
Y_Dependent

#Scatter Plot
plt.scatter(X_Explanatory,Y_Dependent)
plt.show
"""
Always fix the axis and LABEL
"""
plt.scatter(X_Explanatory,Y_Dependent)
plt.axis([0,2500,0,1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
plt.show()
"""
We will add a new constant
"""
X1 = sm.add_constant(X_Explanatory)
reg = sm.OLS(Y_Dependent,X1).fit()
reg.summary()
print(reg.summary())











