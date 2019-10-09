# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:12:16 2019

@author: amitabh.gunjan
"""

tup = 'python', 'geeks'
print(tup)

tup = ('python', 'geeks') 
print(tup) 

# Code for concatenating 2 tuples 
  
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
  
# Concatenating above two 
print(tuple1 + tuple2) 

tuple3 = ('python',)*3
print(tuple3) 

tup4 = ("py") # not a tuple
print(tup4)
isinstance(tup4, tuple)

tup5 = ("py", )
print(tup5)
isinstance(tup5, tuple)

