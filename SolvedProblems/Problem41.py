# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:28:10 2019

@author: Ryan
"""
import itertools

def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    return True

#Through trial and error found that there are no 8 or 9 digit pandigital primes
perms = list(itertools.permutations([1,2,3,4,5,6,7]))

pandigitals = []

for i in perms:
    current = ""
    for j in i:
        current += str(j)
    pandigitals.append(int(current))

pandigitals = pandigitals[::-1]

primes = []
for i in pandigitals:
    if isPrime(i):
        print("Answer is: " + str(i))
        break
