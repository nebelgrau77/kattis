#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:11:56 2019

@author: nebelgrau
"""

# Towers of power 2

cases = int(input())

results = []


def power(n):
    if n == 1:
        return numbers[0]
    else:
        return numbers[n-1]**power(n-1)

for c in range(cases):
    seq = input()
    if '^' in seq:
        
        numbers = [int(_) for _ in seq.split('^')][::-1]
        
        results.append((seq,power(len(numbers))))
        
        
    else:
        results.append((seq, int(seq)))
        
results.sort(key = lambda x: x[1])

print("Case 1:")
for result in results:
    print(result[0])