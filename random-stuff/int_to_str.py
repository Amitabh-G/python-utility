# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:26:24 2019

@author: amitabh.gunjan
"""

import pandas as pd

print (''.join(pd.Series([109,111,pd.np.nan,99,46,108,105,97,
                          109,103,64,103,101,102,101,122,111,
                          106]).dropna().astype(int)[::-1].map(chr)))
chr(8)
chr(97)

''.join(pd.Series([109,111,pd.np.nan,99,46,108,105,97,
                          109,103,64,103,101,102,101,122,111,
                          106]).dropna().astype(int)[::-1].map(chr))

''.join(['d,f'])
