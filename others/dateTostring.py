# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:54:38 2018

@author: amitabh.gunjan
"""
import datetime
from datetime import datetime, timedelta

a = "03/12/2018"
date_format = "%d/%m/%Y"

t = datetime.strptime(a, date_format)
end_date = t + timedelta(days=10)
end_date


s = end_date.strftime('%m/%d/%Y')
s
print(type(s))


#date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")




a.split('/')
print(a)
print(a.split('/')[0])

int(a.split('/')[0])
b = int(a.split('/')[0]) + 1
b

#b = map(int, a.split('/')[0])
#b
#print(b)
