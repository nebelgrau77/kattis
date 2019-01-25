#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:37:05 2019

@author: nebelgrau
"""

# The Amazing Human Canonball

from math import sin, cos, radians
n = int(input())

for _ in range(n):
    v0, theta, x1, h1, h2 = map(float, input().split())
    t1 = x1/(v0*cos(radians(theta)))
    y = v0*t1*sin(radians(theta))-0.5*9.81*(t1**2)
    if y > h1+1 and y < h2-1:
        print('Safe')
    else:
        print('Not Safe')