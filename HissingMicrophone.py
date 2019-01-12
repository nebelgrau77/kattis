#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:21:50 2019

@author: nebelgrau
"""

word = input()

def detection(word):
    sounds = [letter for letter in word]
    for n in range(1, len(sounds)):
        if sounds[n] == 's' and sounds[n-1] == 's':
            return True
    return False

if detection(word) == True:
    print('hiss')
else:
    print('no hiss')