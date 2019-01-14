# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:12:57 2019

@author: nebelgrau
"""

# Railroad

junctions, switches = map(int, input().split())

if switches%2 == 0:
    print('possible')
else:
    print('impossible')