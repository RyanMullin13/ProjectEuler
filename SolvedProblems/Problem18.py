# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:35:38 2019

@author: Ryan
"""

file = open("Problem18Data.txt")
nums = []
for i in file:
    nums.append([int(i) for i in i.rstrip('\n').split(" ")])


    

def rowMax(a,b):
    for i in range(len(a)):
        a[i] = max(  (a[i] + b[i]) , (a[i] + b[i+1]) )
    return a

def triangleMax(triangle):
    row = len(triangle) - 2
    
    while len(triangle[row]) > 1:
        triangle[row] = rowMax(triangle[row], triangle[row + 1])
        row -= 1
    return rowMax(triangle[0],triangle[1])[0]
    
ans = triangleMax(nums)

print("Answer is: " + str(ans))

file.close()