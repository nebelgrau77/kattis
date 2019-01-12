#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:53:38 2019

@author: nebelgrau
"""

#Trik

moves = input()

cups = [1,0,0] # initial position, ball under the cup on the left

for move in moves:
    if move == 'A':
        cups[0], cups[1] = cups[1], cups[0] #left and central cups switched
    elif move == 'B':
        cups[1],cups[2] = cups[2],cups[1] #central and right cups switched
    else:
        cups[0], cups[2] = cups[2],cups[0] #right and left cups switched
        
print((cups.index(1))+1) #return number 1, 2 or 3