# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:25:19 2019

@author: Ryan
"""

MAX = 1000000
primes = []

def Sieve():
    isComposite = [False]*(MAX+1)
    i = 2
    while(i * i <= MAX):
        if(isComposite[i] == False):
            j = 2
            while(j * i <= MAX):
                isComposite[i * j] = True
                j+=1
        i += 1
    for i in range(2,MAX+1):
        if (isComposite[i]==False):
            primes.append(i)

Sieve()
def nstPrime(n):
    return primes[n-1]

answer = nstPrime(10001)

print(str(answer))