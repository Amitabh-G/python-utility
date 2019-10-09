# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:20:11 2019

@author: amitabh.gunjan
"""

#import dask_ml.joblib  # registers joblib plugin
# Scikit-learn bundles joblib, so you need to import from
# `sklearn.externals.joblib` instead of `joblib` directly
#from sklearn.externals.joblib import parallel_backend
from sklearn.datasets import load_digits
#from sklearn.grid_search import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV

from sklearn.svm import SVC
import numpy as np

from dask.distributed import Client
from sklearn.externals import joblib

digits = load_digits()

param_space = {
    'C': np.logspace(-6, 6, 13),
    'gamma': np.logspace(-8, 8, 17),
    'tol': np.logspace(-4, -1, 4),
    'class_weight': [None, 'balanced'],
}

model = SVC(kernel='rbf')
search = RandomizedSearchCV(model, param_space, cv=3, n_iter=50, verbose=10)

client = Client()
with joblib.parallel_backend('dask'):
    search.fit(digits.data, digits.target)