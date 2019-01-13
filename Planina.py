#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:32:36 2019

@author: nebelgrau
"""

# Planina

i = int(input())

side_points = 2 # side of the initial 4 point square

for n in range(i):
    side_points = side_points + (side_points-1) # put a point in between every two points
    
print(side_points**2) # return the square