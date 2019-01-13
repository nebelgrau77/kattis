#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:09:15 2019

@author: nebelgrau
"""

# Cold-puter Science

_ = input()
temperatures = [int(x) for x in input().split()]
subzero = [t for t in temperatures if t < 0]

print(len(subzero))