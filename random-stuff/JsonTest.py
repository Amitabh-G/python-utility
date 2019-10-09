# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:41:21 2018

@author: amitabh.gunjan
"""

import json
from pprint import pprint

#with open('E:/OptionPricing/JSON/TempData.json') as f:
#    data = json.load(f)

#pprint(data)
#
#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]


with open('E:/OptionPricing/Input.json') as f:
    data = json.load(f)

pprint(data)

data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]

data[0]['asset']
data[1]

for i in (1:range(data[0])):
    print(data[0][i])