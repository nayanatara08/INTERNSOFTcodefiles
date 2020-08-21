# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('AAPL Historical Data.csv',usecols = [0,1,2,3,4])

X_Axis = dataset[['Price','Open','High','Low']].mean(axis = 1)

Y_Axis = np.arange(1,len(dataset)+1,1)

plt.plot(X_Axis,Y_Axis,'r',label = 'My Plot')
