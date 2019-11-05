# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:42:12 2019

@author: amitabh.gunjan
"""


df={'time':[1,1,1],'counter':['A','B','C'],'ID':[0,0,0],'value':[1,1,3]}
df = pd.DataFrame(df)
import pandas as pd
df
pd.pivot_table(df, columns=['counter'], index=['ID', 'time'], values='value').reset_index()

df.pivot_table(columns='counter',index=['ID','time'],values='value').reset_index()


# Numpy reshape

a = [1,2,3,4,5,6]
seq_length= 1
import numpy as np
a_reshaped = np.reshape(a, (len(a), seq_length, 1))
a_reshaped
