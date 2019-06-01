# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:02:54 2019

@author: Ryan
"""

def sumOfDivisors(n):
    divisors = []
    for i in range(1,n):
        if(n%i == 0):
            divisors.append(i)
    return sum(divisors)
def isAmicable(n):
    return sumOfDivisors(sumOfDivisors(n)) == n and sumOfDivisors(n) != n

amicables = []

for i in range(1,10000):
    if isAmicable(i):
        amicables.append(i)
answer = sum(amicables)

print("Answer is: " + str(answer))