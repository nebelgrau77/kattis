# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:27:48 2019

@author: nebelgrau
"""

# Judging Moose

(l,r) = map(int, input().split())

if l == r == 0:
    print('Not a moose')
elif l == r:
    print('Even', l+r)
else:
    print('Odd', 2 * max(l,r))