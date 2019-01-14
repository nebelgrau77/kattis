# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:47:22 2019

@author: nebelgrau
"""

# Stand on Zanzibar

n = int(input())

for _ in range(n):
    numbers = [int(x) for x in input().split()]
    bound = 0
    for i in range(len(numbers[:-1])):
        if numbers[i+1] > 2 * numbers[i]:
            bound = bound + numbers[i+1] - 2*numbers[i]
    
    
    print(bound)