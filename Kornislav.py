# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:06:34 2019

@author: nebelgrau
"""

# Kornislav

numbers = [int(_) for _ in input().split()]

from itertools import permutations

choices = []

for p in permutations(numbers, 4): # get all the possible orders of turtle's steps
    choices.append(p)

solutions = []
    
for c in choices:
    if c[0] >= c[2] and c[1] <= c[3]: # find those where the rectangle will be closed
        area = min(c[0],c[2]) * min(c[1],c[3]) # calculate the rectangle area
        solutions.append(area)
        
print(max(solutions)) # return the biggest possible area