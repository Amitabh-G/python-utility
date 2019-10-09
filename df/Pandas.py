# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:39:10 2018

@author: amitabh.gunjan
"""
import numpy as np
import pandas as pd
n = NaN
n = np.nan
n
#data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#        'year': [2012, 2012, 2013, 2014, 2014], 
#        'reports': [4, 24, 31, 2, 3]
#        }
#df1 = pd.DataFrame([[1,2],[4,3]])
df1 = pd.DataFrame([[1,2],[4,'a']])   ### Now type is an object
df2 = pd.DataFrame([[1,.2],[4,3]])
df3 = pd.DataFrame([[1,5],[4,3]])
#print( map(type,df1[1]))
#df1.values
#df1.describe
#df1.abs
#df1.aggregate
#df1.info()
#df2.asfreq
#df2.any
#df2.boxplot
#df2.count()
#df2.count(axis = 1)
#df1.count()
#df1.dtypes()
#df2.dtypes
#df3.dtypes
#df1.dtypes
#df1[1] = df1[1].str.replace('a', '6')
df1
df1.replace(to_replace='a', value=np.nan, inplace=False, limit=None, regex=False, method='pad', axis=None)
#df1.replace(to_replace= 'NaN', value= df1[:1].mean(), inplace=False, limit=None, regex=False, method='pad', axis=None)
#df1.mean(axis = 1)
#df3.mean(axis = 1)
#df3
#df3.mean(axis = 0)
#df1.mean(axis = 0)
#df1.mean()
#
#df1.iloc[1].fillna(df1.iloc[1].mean().dropna(axis = 1, how = 'all'))
#

df1 = df1.replace(to_replace='a', value=np.nan, inplace=False, limit=None, regex=False, method='pad', axis=None)
df1
ColToRplc = df1[1]
ColToRplc = np.array(ColToRplc)
ColToRplc
ColToRplc.mean()
print(np.nanmean(ColToRplc))
MeanColToRplc = np.nanmean(ColToRplc)
MeanColToRplc
#df1.replace({'a': '3'}, regex=True)


df1 = df1.fillna(value = MeanColToRplc)
df1
#def fillWithMean(df):
#    
#    return df.fillna(df.mean()).dropna(axis=1, how='all')
#def FillMean(Data):
#    return Data.fillna(Data.mean().dropna(axis = 1, how = 'all'))