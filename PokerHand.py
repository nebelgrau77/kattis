# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:07:28 2019

@author: nebelgrau
"""

# Poker Hand

ranks = [card[0] for card in input().split()] # make a list of ranks
    
counts = []
for rank in set(ranks):
    counts.append(ranks.count(rank)) # make a list of counts of various ranks
    
print(max(counts))