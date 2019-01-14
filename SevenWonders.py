# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:16:40 2019

@author: nebelgrau
"""

# Seven Wonders

cards = [_ for _ in input()]

T = 0
C = 0
G = 0

for card in cards:
    if card == 'T':
        T += 1
    elif card == 'C':
        C += 1
    else:
        G += 1
    
card_points = T**2 + C**2 + G**2 + min(T,C,G)*7

print(card_points)