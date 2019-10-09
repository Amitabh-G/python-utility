# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:09:59 2018

@author: amitabh.gunjan
"""
import pandas as pd

s = pd.Series(list('abca'))
s
dummy = pd.get_dummies(s)
dummy
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'], 'C': [1, 2, 3]})
pd.get_dummies(df)
