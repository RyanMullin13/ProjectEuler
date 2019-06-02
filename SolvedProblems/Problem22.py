#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:25:59 2019

@author: ryan
"""
from string import ascii_uppercase

file = open("Problem22Data.txt")

for i in file:
    names = i.split(",")
for i in range(len(names)):
    names[i] = names[i].strip('"')

names.sort()

letters = []
for i in ascii_uppercase:
    letters.append(i)
nums = list(range(1,27))

value = dict(zip(letters,nums))

answer = 0

for i in range(len(names)):
    for j in names[i]:
        answer += (i+1) * value[j]
print("Answer is: " + str(answer))