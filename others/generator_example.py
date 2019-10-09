# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:21:28 2019

@author: amitabh.gunjan
"""

def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 