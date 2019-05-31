# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:29:20 2019

@author: Ryan
"""

import math

fact = 2 ** 1000

fact = str(fact)

total = 0
for i in fact:
    total += int(i)

print("Answer is: " + str(total))