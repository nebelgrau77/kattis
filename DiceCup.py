#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:32:22 2019

@author: nebelgrau
"""

# Dice Cup

dice1, dice2 =  map(int, input().split())

outcomes = [d1+d2 for d1 in range(1,dice1+1) for d2 in range(1,dice2+1)]
#all possible combinations between the dice

combos = set(outcomes)
#each just once

probabilities = {}

# check if there's already a combo with a given probability(count)
# if not, create it, otherwise append the combo to the list

for combo in combos:
    if outcomes.count(combo) in probabilities.keys():
        probabilities[outcomes.count(combo)].append(combo)
    else:
        probabilities[outcomes.count(combo)] = [combo]
    
best_result = max(probabilities.keys())

for _ in probabilities[best_result]:
    print(_)