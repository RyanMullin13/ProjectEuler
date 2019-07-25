# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:27:06 2019

@author: Ryan
"""

def isPandigital(n):
    n = str(n)
    digits = len(n)
    
    if digits >= 10 or digits < 9:
        return False

    for i in range(1,10):
        if str(i) not in n:
            return False
    return True

def makesPandigitalProductIdentity(a,b):
    number = str(a) + str(b) + str(a*b)
    
    return isPandigital(int(number))

products = []
for a in range(0,100000):
    for b in range(a,100000):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if makesPandigitalProductIdentity(a,b):
            products.append(a*b)
answer = sum(set(products))
print("Answer is: " + str(answer))