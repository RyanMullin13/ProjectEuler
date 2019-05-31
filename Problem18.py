# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:35:38 2019

@author: Ryan
"""

file = open("Problem18Data.txt")
nums = []
for i in file:
    nums.append([int(i) for i in i.rstrip('\n').split(" ")])

