#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:19:05 2019

@author: ryan
"""

def isPalindrome(n):
    num = str(n)
    reverse = num[::-1]
    
    return(num == reverse)

palindromes = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if isPalindrome(i*j):
            palindromes.append(i*j)
print("Largest Palindrome Product: " + str(max(palindromes)))
    

