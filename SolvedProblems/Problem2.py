#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:15:08 2019

@author: ryan
"""
#Generate a Fibonacci Sequence in a list upto MAX number
def Fib(MAX):
    FibSeq = [1,1]

    while max(FibSeq) < MAX:
        tail1 = FibSeq[len(FibSeq) - 1]
        tail2 = FibSeq[len(FibSeq) - 2]
        
        FibSeq.append(tail1 + tail2)
    
    return FibSeq



ans = Fib(4000000)

#Add all even Fibonacci Numbers
total = 0
for i in ans:
    if i%2 == 0:
        total += i

    
    