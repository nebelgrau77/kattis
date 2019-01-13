#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:27:21 2019

@author: nebelgrau
"""

# free food

n = int(input())

free_food_days = []
for i in range(n):
    start, end = [int(x) for x in input().split()]
    event_days = [_ for _ in range(start, end+1)]
    free_food_days += event_days
    
print(len(set(free_food_days)))