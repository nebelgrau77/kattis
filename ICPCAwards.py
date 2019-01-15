# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:03:48 2019

@author: nebelgrau
"""

# ICPC awards

teams = int(input())
winners = []
unis = []
for i in range(teams):
    uni, team = map(str, input().split())
    if uni not in unis:
        print(uni, team)
        unis.append(uni)
    if len(unis) == 12:
        break