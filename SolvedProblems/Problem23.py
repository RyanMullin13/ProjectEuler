# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:57:43 2019

@author: Ryan
"""

def isAbundant(n):
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    return sum(divisors) > n

abundants = []
for i in range(1,28124):
    if isAbundant(i):
        abundants.append(i)
nonAbs = [i for i in range(28124)]

for i in range(len(abundants)):
    for j in range(i,len(abundants)):
        if abundants[i] + abundants[j] < 28124:
            nonAbs[abundants[i] + abundants[j]] = 0

answer = sum(nonAbs)
print("Answer is: " + str(answer))