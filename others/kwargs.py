# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:09:47 2018

@author: amitabh.gunjan
"""

def my_function(**kwargs):
    print(kwargs)

my_function(a=12, b="abc")
my_function(a = 15, b = 87, v = 'fff', l = 4*8)

def my_function_1(a, b, **kwargs):
    z = a**b
    print(a, 'raised to ', b, 'is: ', z)
    print(kwargs)
    print(a+b)

my_function_1(4, 2, f = 34, h = 'bjhjighusgughsagctfsdugcd')

def mean_fn(**kwargs):
    c = sum(kwargs.values())/len(kwargs)
    print(c)
    return(c)
    
mean_fn(a = 12, b = 24, c = 46)

def mean_fn_pos(m, n):
    return((m+n)/2)

def Call_a_func(fnc, m, n):
    return(fnc(m, n))
    
print(Call_a_func(mean_fn_pos, 2, 3))
    
    