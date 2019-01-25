#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:03:20 2019

@author: nebelgrau
"""

# No Duplicates

words = [_ for _ in input().split()]

if len(words) == len(set(words)):
    print('yes')
else:
    print('no')