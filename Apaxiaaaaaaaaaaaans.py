#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:22:17 2019

@author: nebelgrau
"""

# Apaxiaaaaaaaaaaaans!

name = input()
letters = [_ for _ in name]

compact = []

for n in range(len(letters)):
    if n == 0:
        compact.append(letters[n])
    
    elif letters[n] != letters[n-1]:
        compact.append(letters[n])

print(''.join(compact))