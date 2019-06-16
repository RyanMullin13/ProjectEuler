# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:13:50 2019

@author: Ryan
"""

def findPrimes(n):
    primes = list(range(2,n+1))
    
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i*j)
            j += 1
    return primes
primes = findPrimes(50)