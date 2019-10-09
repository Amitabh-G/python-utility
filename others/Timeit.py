# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:06:38 2018

@author: amitabh.gunjan
"""

import timeit
print(timeit.timeit("math.pow(2, 100)",setup='import math'))
print(timeit.timeit("2.0 ** 100.0"))
print(timeit.timeit("2 ** 100"))
print(timeit.timeit("2.01 ** 100.01"))