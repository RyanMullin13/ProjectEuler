# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:24:36 2019

@author: Ryan
"""

def collatzLen(n):
    terms = 1
    
    while(n != 1):
        if(n%2 == 0):
            n = n/2
            terms +=1
        else:
            n = (3*n) + 1
            terms += 1
    return terms

largest = 0
startingNum = 0
for i in range(1000000,1,-1):
    current = collatzLen(i)
    if current > largest:
        largest = current
        startingNum = i
print("Answer is: " + startingNum)