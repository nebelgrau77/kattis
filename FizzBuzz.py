#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:20:47 2019

@author: nebelgrau
"""

# FizzBuzz

x,y,n = map(int,input().split())

for i in range(1,n+1):
    if i%x == 0 and i%y == 0:
        print('FizzBuzz')
    elif i%x == 0 and i%y != 0:
        print('Fizz')
    elif i%x != 0 and i%y == 0:
        print('Buzz')
    else:
        print(i)