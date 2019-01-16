#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:11:19 2019

@author: nebelgrau
"""

# Towers of power 2

cases = int(input())

results = []

for c in range(cases):
    seq = input()
    if '^' in seq:
        
        numbers = [int(_) for _ in seq.split('^')]
        
        tower = numbers[0]
        
        for i in range(1,len(numbers)):
            tower = tower ** numbers[i]
        
        results.append((seq,tower))

    else:
        results.append((seq, int(seq)))
        
results.sort(key = lambda x: x[1])

print("Case 1:")
for result in results:
    print(result[0])
        