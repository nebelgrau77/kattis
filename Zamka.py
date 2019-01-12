#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:55:48 2019

@author: nebelgrau
"""

#Zamka

l = int(input())
d = int(input())
x = int(input())

solutions = []
for n in range(l,d+1):
    digits = [_ for _ in str(n)]
    if sum([int(_) for _ in digits]) == x: #find all n numbers where l<n<d 
                                           # where sum of digits equals x
        solutions.append(n)
print(min(solutions))
print(max(solutions))



