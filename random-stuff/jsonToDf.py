# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:13:26 2019

@author: amitabh.gunjan
"""

a = [
    {
        "Names": [
            "James",
            "Bob",
            "David"
        ],
        "Salary": [
            "2000$",
            "5000$",
            "6000$"
        ],
        "Id": [
            "1",
            "2",
            "3"
        ]
    },
    {
        "Names": [
            "John",
            "Charles",
            "Harry"
        ],
        "Salary": [
            "1000$",
            "2000$",
            "3000$"
        ],
        "Id": [
            "4",
            "5",
            "6"
        ]
    }
]
    
    
import pandas as pd 
pd.io.json.json_normalize(a)
names_df = pd.io.json.json_normalize(a, 'Names')
id_df = pd.io.json.json_normalize(a, 'Id')
Salary_df = pd.io.json.json_normalize(a, 'Salary')
frames = [names_df, id_df, Salary_df]
final_df = pd.concat(frames, axis = 1)
final_df.columns = ['Names', 'Id', 'Salary']

# Another method
col_names = [k for k,v in a[0].items()]
frames = [pd.io.json.json_normalize(a, str(col)) for col in col_names]
final_df = pd.concat(frames, axis = 1)
final_df.columns = col_names

final_df













