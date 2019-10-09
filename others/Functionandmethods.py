# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:58:32 2018

@author: amitabh.gunjan
"""

import inspect

class OOP:
    
    def __init__(self):
        pass
    
    @staticmethod
    
    def statMeth():
        pass
      
    @classmethod
    
    def classMeth(cls):
        pass
    
    
    def instanceMeth(self):
        pass
        
    


a = OOP()
inspect.ismethod(a.instanceMeth)
inspect.ismethod(a.statMeth)
inspect.ismethod(a.classMeth)

inspect.isfunction(a.instanceMeth)
inspect.isfunction(a.statMeth)
inspect.isfunction(a.classMeth)

inspect.ismethod(OOP.instanceMeth)
inspect.ismethod(OOP.statMeth)
inspect.ismethod(OOP.classMeth)


inspect.isfunction(OOP.instanceMeth)
inspect.isfunction(OOP.statMeth)
inspect.isfunction(OOP.classMeth)





def outsideClass():
    return(2)


call = outsideClass
print(call)


inspect.ismethod(outsideClass)
inspect.isfunction(outsideClass)

class Sub(OOP):
    def __init__(self):
        super().__init__(self)
        pass
    
    def instanceMethSubclass():
        pass
    
    @staticmethod
    
    def staticMethSubclass():
        pass


inspect.isfunction(Sub.instanceMeth)
inspect.isfunction(Sub.staticMethSubclass)
inspect.isfunction(Sub.instanceMethSubclass)

inspect.ismethod(Sub.instanceMeth)
inspect.ismethod(Sub.staticMethSubclass)
inspect.ismethod(Sub.instanceMethSubclass)


