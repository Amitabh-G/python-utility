# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:24:58 2018

@author: amitabh.gunjan
"""
##########################
### Immutables in python.
### They are:
### string
### tuples
### integer
### float
### boolean
### frozenset
##########################
### string
###########

s = 'ag'
s = s+ 'd'
s[1]
# The below assignment raises an error. The string object can't be changed in place.
s[1] = 't'
s[0]
s[0] = 'p'

###########
### tuples
###########
t = (1, 2, 3)
t[0]

# The below assignment raises an error. The tuple object can't be changed in place.
t[0] = 4
t[3] = 7
t1 = (4, 5, 6)
t2 = t + t1
t2
