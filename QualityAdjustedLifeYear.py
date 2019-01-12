#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:24:51 2019

@author: nebelgrau
"""

#Quality Adjusted Life Year

n = int(input())
qaly = 0
for _ in range(n):
    x,y = map(float, input().split())
    qaly += x*y
print("%.3f" % qaly)