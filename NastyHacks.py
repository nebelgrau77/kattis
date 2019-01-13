#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:42:45 2019

@author: nebelgrau
"""

# nasty hacks

results = []
for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if r == (e-c):
        results.append('does not matter') 
    # revenue w/o advertising same as with advertising minus advertising cost
    elif r < (e-c):
        results.append('advertise')
    
    else:
        results.append('do not advertise')

for result in results:
    print(result)