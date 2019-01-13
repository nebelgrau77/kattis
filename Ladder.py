#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:59:04 2019

@author: nebelgrau
"""

h,v = map(int, input().split())
from math import sin, radians

length = -(-h//sin(radians(v)))  #floor division rounds down

print (int(length)) # convert to int