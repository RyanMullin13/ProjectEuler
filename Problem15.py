# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:33:34 2019

@author: Ryan
"""

import math

def possibleRoutes(size):
    grid = [1] * size
    
    for i in range(size):
        for j in range(i):
            grid[j] = grid[j] + grid[j-1]
        grid[i] = 2 * grid[i - 1]
    return grid[size - 1]

ans = possibleRoutes(20)
    