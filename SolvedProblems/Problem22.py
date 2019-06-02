#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:25:59 2019

@author: ryan
"""

file = open("Problem22Data.txt")

for i in file:
    names = i.split(",")
for i in range(len(names) - 1):
    names[i] = names[i].strip('"')
