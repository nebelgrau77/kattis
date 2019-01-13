#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:33:42 2019

@author: nebelgrau
"""

# Pet

results = {}
for n in range(5):
    points = sum([int(x) for x in input().split()])
    results[points] = n

best_result = max(results.keys())
best_contestant = results[max(results.keys())]+1
    
print(best_contestant, best_result)