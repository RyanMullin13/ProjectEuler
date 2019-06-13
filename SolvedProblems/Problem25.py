# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:38:16 2019

@author: Ryan
"""

f1 = 1
f2 = 1

temp = 0
i = 2
while len(str(temp)) != 1000:
    
    temp = f1 + f2
    f1 = f2
    f2 = temp
    
    i+=1
    
print("Answer is: " + str(i))