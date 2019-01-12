#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:26:02 2019

@author: nebelgrau
"""
# Provinces and Gold

cards = [int(x) for x in input().split()]

victory = {8:'Province',5:'Duchy',2:'Estate'}
treasure = {6:'Gold',3:'Silver',0:'Copper'}

total_value = cards[0]*3 + cards[1]*2 + cards[2]*1


vic_possible = {} # possible victory cards you can buy
for k in victory.keys():
    if k <= total_value:
        vic_possible[k] = victory[k]

        
tre_possible = {} # possible treasure cards you can buy
for k in treasure.keys():
    if k <= total_value:
        tre_possible[k] = treasure[k]


if len(vic_possible) > 0:
    print(vic_possible[max(vic_possible.keys())],"or",tre_possible[max(tre_possible.keys())])
else:
    print(tre_possible[max(tre_possible.keys())])