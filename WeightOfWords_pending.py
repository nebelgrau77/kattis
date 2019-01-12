#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:17:16 2019

@author: nebelgrau
"""

# The Weight of Words

l, w = [int(x) for x in input().split()]
    
current_weight = 0
values = dict(zip([_ for _ in range(1,27)], 'abcdefghijklmnopqrstuvwxyz'))
letters = []
a = 26
    
while len(letters) < l:
    if len(letters) + 1 <= l:
        if current_weight + a <= w and (w - (current_weight+a)) >= (length - len(letters)+1):
            current_weight += a
            letters.append(values[a])
        else:
            a = a - 1
    
if len(letters) == l and current_weight == w:
    print(''.join(letters))    
else:
    print('impossible')
    
    
# it does work with the test cases, but was not accepted by Kattis