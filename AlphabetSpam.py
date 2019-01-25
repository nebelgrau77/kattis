#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:36:39 2019

@author: nebelgrau
"""

# Alphabet Spam

spam = input()
letters = [_ for _ in spam]

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for letter in letters:
    if letter.islower() == True:
        lowercase += 1
    elif letter.isupper() == True:
        uppercase += 1
    elif letter == '_':
        whitespace += 1
    else:
        symbols += 1

print(whitespace/len(letters))
print(lowercase/len(letters))
print(uppercase/len(letters))
print(symbols/len(letters))