# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:18:49 2019

@author: amitabh.gunjan
"""

import _pickle as cPickle

model_path = "D:/work/recommendation-system/ml-based/CTRM-ML/ml-recommendation/models-and-data/reference/467a28cc-bc93-4e38-8ff5-0a56ae128f3b/23/model"

with open(model_path, 'rb') as model:
    model_all_users = cPickle.load(model)
    model.close()

print(model_all_users)

a = ["a", 1, 2]
isinstance(a, type(None))
all(v is not isinstance(v, type(None)) for v in a)
all(v is isinstance(v, type(None)) for v in a)
ab = (v is not isinstance(v, type(None)) for v in a)
b = ['1', None]
print(b)
n = object()
print(n)
print(" ")

a_l = [1,2,3]
b = a_l[:6]
b
listOflists = [[1,2,3], [8,5,4,2], [0,9], [1,3,6,8,3,5]]
len(listOflists)

def get_longest_list(listOflists):
    count = []
    for i in listOflists:
        count.append(len(i))
    idx = count.index(max(count))
    return listOflists[idx]
    
long_list = get_longest_list(listOflists)
print(long_list)






help(["foo", "bar", "baz"])
help(())
    