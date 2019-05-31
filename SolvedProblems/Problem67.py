# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:58:15 2019

@author: Ryan
"""

from Problem18 import rowMax,triangleMax

a = [1,2,3]
b = [1,2,3,4]

file = open("Problem67Data.txt")

nums = []
for i in file:
    nums.append([int(i) for i in i.rstrip('\n').split(" ")])
answer = triangleMax(nums)

print("Answer is: " + str(answer))