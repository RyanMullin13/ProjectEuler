#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:36:14 2019

@author: ryan
"""

def is_prime(n):
    prime = True
    for i in range(2,n):
        if(n%i == 0):
            prime = False
    return prime

def find_primes(limit):
    primes = []
    for i in range(1,limit+1):
        if is_prime(i):
            primes.append(i)
    return primes

def is_power(x,y):
    if(x == 1):
        return (y==1)
    pow = 1
    while (pow < y):
        pow = pow * x
    return(pow == y)
    
def smallest_evenly_divisible(n):
    num = 1
    primes = find_primes(n)
    
    for i in range(n+1,1,-1):
        for j in primes:
            if(is_power(j,i)):
                num *= i
                primes.remove(j)
    
    return num  
    
ans = smallest_evenly_divisible(20)

print(str(ans) + " is the smallest posive number evenly divisible by all numbers 1 to 20")
