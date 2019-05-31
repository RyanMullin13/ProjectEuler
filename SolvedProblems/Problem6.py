#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 08:58:55 2019

@author: ryan
"""

import numpy as np
lst = [range(1,101)]

lst = np.array(lst)

squareOfSum = (np.sum(lst)) ** 2

squares = lst * lst

sumOfSquare = np.sum(squares)

dif = int(squareOfSum - sumOfSquare)

print("Answer is " + str(dif))