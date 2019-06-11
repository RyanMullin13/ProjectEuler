# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:22:54 2019

@author: Ryan
"""

from itertools import permutations

perm = list(permutations([0,1,2,3,4,5,6,7,8,9]))

target = perm[1000000 - 1]

answer = ''
for i in target:
    answer += str(i)
print("Answer is: " + answer)