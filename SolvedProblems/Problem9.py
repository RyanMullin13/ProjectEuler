# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:27:52 2019

@author: Ryan
"""

import math

for a in range(1,501):
    for b in range(1,501):
        c = 1000 - a - b
        if((c**2) == (a**2 + b**2)):
            print("Answer is: " + str(a*b*c))