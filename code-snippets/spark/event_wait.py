# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:21:39 2019

@author: amitabh.gunjan
"""

from random import random
import threading
import time

result = None

def background_calculation():
    # here goes some long calculation
    time.sleep(random() * 5 * 60)

    # when the calculation is done, the result is stored in a global variable
    global result
    result = 42

def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # wait here for the result to be available before continuing
    thread.join()

    print('The result is', result)

if __name__ == '__main__':
    main()