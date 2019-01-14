# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:19:56 2019

@author: nebelgrau
"""

# Parking

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    stores = [int(_) for _ in input().split()]
    stores.sort(reverse = True) # shortest distance if stores are in order
    distance = 0
    for i in range(n):
        distance += abs(stores[i] - stores[i-1])
    print(distance)