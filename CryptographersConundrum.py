#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:06:27 2019

@author: nebelgrau
"""

# Cryptographer's Conundrum

letters = [_ for _ in input()]

days = 0
for l in range(len(letters)):
    
    if l%3 == 0 and letters[l] != 'P':
        days += 1
    elif l%3 == 1 and letters[l] != 'E':
        days += 1
    elif l%3 == 2 and letters[l]!= 'R':
        days += 1
           
print(days)