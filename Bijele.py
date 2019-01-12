#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:03:47 2019

@author: nebelgrau
"""

#Bijele

# king, queen, rooks, bishops, knights, pawns
ki,qu,ro,bi,kn,pa = map(int, input().split())

print(1-ki,1-qu,2-ro,2-bi,2-kn,8-pa)