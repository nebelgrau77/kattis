#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:21:48 2019

@author: nebelgrau
"""

# Last Factorial Digit

def factorial(n):
    s = 1
    for i in range (1,n+1):
        s = s * i
    return s
def last_digit(num):
    s = str(num)
    return s[-1]
T = int(input())
for _ in range(T):
    f = factorial(int(input()))
    l = last_digit(f)
    print(int(l))