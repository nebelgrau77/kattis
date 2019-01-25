#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:13:56 2019

@author: nebelgrau
"""

# Modulo

numbers = []
for _ in range(10):
    numbers.append(int(input())%42)

print(len(set(numbers)))