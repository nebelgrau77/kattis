#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 09:11:21 2019

@author: nebelgrau
"""

# Pot

n = int(input())

result = 0

for i in range(n):
    digits = [x for x in input()]
    number = int(''.join(digits[:-1]))
    power = int(''.join(digits[-1:]))
    result += number ** power

print(result)