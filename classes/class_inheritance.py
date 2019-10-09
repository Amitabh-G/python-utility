# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:54:31 2018

@author: amitabh.gunjan
"""
class integer:
    
    def __init__(self, num):
        self.num = num
        
    def Square(self):
        pass


class IntSquare(integer):
    
    def Square(self, num):
        
        print(num**2)
        return(num**2)
        

a = integer(1)
a.Square()
asq = IntSquare(a)

asq.Square(2)
asq.Square()
