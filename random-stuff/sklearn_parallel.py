# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:39:52 2019

@author: amitabh.gunjan
"""

from operator import neg
from sklearn.utils import parallel_backend, Parallel, delayed
import joblib


with parallel_backend('threading'):
    print(joblib.Parallel()(joblib.delayed(neg)(i + 1) for i in range(5)))
    
