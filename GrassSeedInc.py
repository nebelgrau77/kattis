#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:16:41 2019

@author: nebelgrau
"""

## Grass Seed Inc.

c = float(input())
l = int(input())
cost = 0
for _ in range(l):
    wi, li = [float(x) for x in input().split()]
    cost = cost + wi*li*c
    
print("%.7f" % cost) 