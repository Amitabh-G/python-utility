# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:41:52 2019

@author: amitabh.gunjan
"""

a = []
if not a:
    print('a has nothing in it.')
else:
    print('something in a')
    
    
def make_batches(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
    


l = [1, 5, 6, 7, 8, 9]

for i in make_batches(range(len(l)), 2):
#    print(list(i))
    print(l[i[0]:i[-1]+1])


for i in range(6):
    print(i, end=', ')
    
import pandas as pd 
  
# intialise data of lists. 
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
df
len(df)
df[0:2]



range(1,10)
print(range(1,10))
list(range(1,10))
