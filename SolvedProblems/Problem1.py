#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:28:23 2019

@author: ryan
"""

answer = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        answer +=i
