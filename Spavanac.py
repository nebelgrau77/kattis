#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:50:16 2019

@author: nebelgrau
"""

# Spavanac

hrs, mins = map(int, input().split())


if mins >= 45:
    hrs = hrs
    mins = mins - 45
else:
    mins = 15 + mins
    if hrs == 0:
        hrs = 23
    else:
        hrs = hrs - 1
print(hrs, mins)