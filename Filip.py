#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:14:02 2019

@author: nebelgrau
"""

# Filip

a, b = input().split()

a1 = int(a[::-1]) #reverse strings, convert to integers
b1 = int(b[::-1])

if a1 > b1:
    print(a1)
else:
    print(b1)