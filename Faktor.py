#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:13:37 2019

@author: nebelgrau

"""

#Faktor 

articles, factor = map(int, input().split())

n = articles * factor

while -(-n//articles) == factor: #floor division "inverted", idea from quora
    n = n - 1
print (n+1)