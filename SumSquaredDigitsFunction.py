#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:51:56 2019

@author: nebelgrau
"""

# Sum Squared Digits Function

for p in range(int(input())):
    k,b,n = [int(x) for x in input().split()]
    digits = []
    for i in range(32,-1,-1):       # conversion to base b
        digits.append(n//(b**i))    # e.g. n // 2**i for binary
        n = n%(b**i)                # what is left
    ssd = sum([d**2 for d in digits])
    print(k, ssd)