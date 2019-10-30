# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:26:33 2019

@author: amitabh.gunjan
"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(4)
s = np.random.uniform(2500,25000000,30)
srtd = np.sort(s)
sqrt = np.sqrt(srtd)
plt.plot(sqrt)
plt.show()
