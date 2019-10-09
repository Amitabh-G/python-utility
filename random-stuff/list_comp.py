# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:58:21 2019

@author: amitabh.gunjan
"""

list_a = [1, 2, 3]
list_b = [2, 7]

tuple_unequal_elem = [(a, b) for a in list_a for b in list_b if a != b]
print(tuple_unequal_elem) # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]
