# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:44:07 2019

@author: Ryan
"""

def Sieve(MAX):
    primes = []
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
    return primes

ans = sum(Sieve(2000000))

print("Answer is: " + str(ans))