# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 01:41:43 2019

@author: amitabh.gunjan
"""

Y = np.reshape(dataX, (int(len(dataX)/seq_length), seq_length))
Y

x = np.array([[[1, 4, 7],
               [2, 5, 8],
               [3, 6, 9]],
              [[10, 40, 70],
               [20, 50, 80],
               [30, 60, 90]],
              [[100, 400, 700],
               [200, 500, 800],
               [300, 600, 900]],
               [[10, 40, 70],
               [20, 50, 80],
               [30, 60, 90]]])
x.shape
x

x = np.array([[[1, 4, 7],
               [2, 5, 8],
               [3, 6, 9]],
              [[10, 40, 70],
               [20, 50, 80],
               [30, 60, 90]],
              [[100, 400, 700],
               [200, 500, 800],
               [300, 600, 900]],
              [[10, 40, 70],
               [20, 50, 80],
               [30, 60, 90]]])

x.shape
