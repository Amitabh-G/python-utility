# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:07:27 2018

@author: amitabh.gunjan
"""

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("echo")
#args = parser.parse_args()
#print(args.echo)
##
##parser.add_argument("square", help = "Computes the square of a number", type = int)
##args1 = parser.parse_args()
##print(args1.square**2)
#
#
#import tensorflow as tf
#tf.app.flags.DEFINE_integer()

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))