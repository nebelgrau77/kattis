#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:50:11 2019

@author: misiek
"""

# Sibice / Matches

n, w, h = map(int, input().split())
answers = []
for i in range(n):
    length = int(input())
    if length**2 <= (w**2+h**2): 
    # test if match is shorter than the diagonal
        answers.append('DA')
    else:
        answers.append('NE')
for answer in answers:
    print(answer)