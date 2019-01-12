#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:24:51 2019

@author: nebelgrau
"""

distances = []

n = 0 #initial value for n for the while loop

while n != -1:

    n = int(input())
    total_distance = 0
    current_time = 0
    for line in range(n):
        dist, time = map(int, input().split())
        total_distance = total_distance + dist*(time - current_time)
        current_time = time
    distances.append(total_distance)

for d in distances:
    if d != 0:
        print(d, "miles")
