# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:03:41 2018

@author: amitabh.gunjan
"""
import random as rand
import numpy as np

# Generating random numbers
x = []
y = []
for i in range(100):
    x.append(rand.randint(1, 1000))
    y.append(rand.gauss(1.0, 2.0))


x = np.random.randint(1, 1000, size=100) 
print(x)    
inpt_array = x*5 + np.random.normal(0, 1, size = 100)
print(inpt_array)