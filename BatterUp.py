#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:21:27 2019

@author: nebelgrau
"""

# Batter Up

_ = input()

atbats = [int(x) for x in input().split()]
notwalks = [x for x in atbats if x > -1]

print(sum(notwalks)/len(notwalks))