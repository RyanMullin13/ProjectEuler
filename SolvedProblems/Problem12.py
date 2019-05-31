# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:14:58 2019

@author: Ryan
"""
import math

def divisors(n):
    factors = 0
    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            factors += 2
        else:
            continue
    
    return factors

x = 1

for i in range(2,10000000):
    x+=i
    if divisors(x) > 500:
        break
print("Answer is: " + str(x))