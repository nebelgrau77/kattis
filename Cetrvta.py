#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:06:44 2019

@author: nebelgrau
"""

# Cetvrta

xs = []
ys = []
for _ in range(3):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)
missing_x = [_ for _ in xs if xs.count(_) == 1]
missing_y = [_ for _ in ys if ys.count(_) == 1]

print(missing_x[0], missing_y[0])