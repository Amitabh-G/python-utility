# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:54:31 2018

@author: amitabh.gunjan
"""
class number:
    # Integer class
    def __init__(self, num):
        self.num = num

    def square(self):
        pass


class int_square(number):
    # Instance of the class integer.
    def square(self, num):
        print(num**2)
        return(num**2)


_num = number(5)
_num_square = int_square(_num)
_num_square.square()
