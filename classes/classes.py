# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:09:18 2018

@author: amitabh.gunjan
"""

class someclass:
    # Class to show class variables and how to modify them.
    classvar = 1

    def _init_(self, Price1, Price2):
        self.Price1 = Price1
        self.Price2 = Price2

    def ChangeVars(self):
        print(self.Price1)
        self.Price1 = 6.0
        print(self.Price1)

    def PrintMeth(self):
        print(self.Price1)



a = someclass(1, 2)
a.ChangeVars()
a.PrintMeth()
a.classvar = 2.0
a.classvar

b = someclass(3, 4)
b.classvar
someclass.classvar





class Office:

    def __init__(self, name):

        self.name = name

    def clean_office(self):

        print('Office of ', self.name, 'must be cleaned in the morning.')

Eka = Office('eka')
Eka.clean_office()

Office.clean_office(Eka)


'''
So Eka.clean_office() implements Office.clean_office(Eka).

We don't actually write instance methods in python. What we write are
class methods. These class methods must take instance as the first
parameter. And therefore instance parameter has to be placed somewhere
explicitly.

'''
