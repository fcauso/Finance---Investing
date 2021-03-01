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