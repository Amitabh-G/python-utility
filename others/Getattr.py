# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:45:34 2018

@author: amitabh.gunjan
"""

class Student:
    
    def __init__(self, standard):
        self.standard = standard

std = Student(5)
__init__ = getattr(std, "__init__")
print(__init__)
print(getattr(std, "standard"))
#for k, v in keyValue:

{k:getattr(std, k) for k,v in keyValue}