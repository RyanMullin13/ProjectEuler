# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:45:09 2019

@author: Ryan
"""

def isSumOfPowers(n,power):
    digits = str(n)
    total = 0
    
    for i in digits:
        total += int(i) ** power
    return total == n

fifthPowers = []

for i in range(2,5*(9**5)):
    if isSumOfPowers(i,5):
        fifthPowers.append(i)
answer = sum(fifthPowers)
print("Answer is: " + answer)