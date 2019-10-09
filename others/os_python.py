# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:37:13 2018

@author: amitabh.gunjan
"""

import os
# A portable way of using operating system dependent functionality.
os.environ.items()
os.environ.keys()

path = os.environ['PATH']
pathList = path.split(';')
cwd = os.getcwd()
print(cwd)

### Make a new directory in the current working directory
newd = os.mkdir('temp-dir')
print(newd)

### List the directory
dirList = os.listdir()
print(dirList)

### Remove the temp-dir from the current directory
os.removedirs('temp-dir')
newdirList = os.listdir()
print(newdirList)


### Create directories on the go.

for i in range(5):
    print(i)
    os.mkdir('temp-dir' + str(i))
    

'temp-dir0' in os.listdir(os.curdir)
### Check the directory list for the new directories
    
os.listdir()

### Remove the directories on the go.
for i in range(5):
    print(i)
    os.removedirs('temp-dir' + str(i))
    
'temp-dir0' in os.listdir(os.curdir)
os.curdir    
os.getcwd()

### common operations on pathnames.
fp = open('junk.txt', 'w')
fp.close()



### File pattern matching

import glob

### Look for the .txt files in the directory.
glob.glob('*.txt')

### Look for the .py files in the directory.
glob.glob('*.py')



### System-specific information related to the Python interpreter.

import sys

sys.platform


