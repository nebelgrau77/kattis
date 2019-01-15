# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:21:15 2019

@author: nebelgrau
"""

# Harshad Numbers

n = int(input())

def is_harshad(number):
    digits = [int(_) for _ in str(number)]
    if number % sum(digits) == 0:
        return True
    else:
        return False

i = n    
while True:
    if is_harshad(i) == True:
        print(i)
        break
    else:
        i = i + 1