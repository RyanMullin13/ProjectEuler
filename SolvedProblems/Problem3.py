#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 05:35:41 2019

@author: ryan
"""
import math

n = 600851475143
primeFactors = []

for i in range(1,int(math.sqrt(n))):
    if(n % i == 0):
        if(isPrime(i)):
            primeFactors.append(i)
        n /= i

print("Largest Prime Factor " + str(max(primeFactors)))

def isPrime(n):
    prime = True
    for i in range(2,n):
        if(n%i == 0):
            prime = False
            break
    return prime
