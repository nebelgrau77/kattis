#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:06:28 2019

@author: nebelgrau
"""

# Datum

# 1 1 is Thursday

day, month = map(int,input().split())


months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# how many days passed since the beginning of the year

days = 0

for i in range(month):
    if months.get(i) == None:
        days = days
    else:
        days += months.get(i)
    
days = days + day

week = ['Wednesday','Thursday','Friday', 'Saturday','Sunday', 'Monday', 'Tuesday']

print(week[days%7]) # what's left after dividing by 7