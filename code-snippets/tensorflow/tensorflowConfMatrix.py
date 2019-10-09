# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:30:45 2018

@author: amitabh.gunjan
"""

import tensorflow as tf     
y = [1, 2, 4]
y_ = [2, 2, 4]

con = tf.confusion_matrix(labels = y_, predictions = y)
sess = tf.Session()
with sess.as_default():
        print(sess.run(con))