# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:25:37 2018

@author: amitabh.gunjan
"""
import tensorflow as tf

hello = tf.constant('Hello Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
