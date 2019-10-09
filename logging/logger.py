# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:24:10 2018

@author: amitabh.gunjan
"""
###############################################################
### Playing with classes. Three classes:
### class demo_logger has some method.
### class two accesses those methods.
### class one creates objects of class demo_logger and passes
### that as an argument to class two, in  turn creating an object 
### of class two. 
### Now, create an object of the class one. It has the attributes
### of class demo_logger. And it also creates an object of class 
### two. So the object of class two can access the methods of 
### class two. This will not work when the argument to the class 
### two constructor is not an instance of class demo_logger.
##################################################################


class demo_logger:
    def write(self, message):
        print(message)

class two:
    def __init__(self, logger):
        self.logger = logger

    def demo_method(self):
        self.logger.write("Class two: demo method is called")

class one:
    logger = demo_logger()
    logger.write("Class one")
    twoObj = two(logger)

oneObject = one()
oneObject.twoObj.demo_method()

oneObject.logger.write("Class one")
oneObject.twoObj.demo_method()















