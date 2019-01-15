# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:04:08 2019

@author: nebelgrau
"""

# Herman

r = int(input())

from math import pi, sqrt

circle = pi * r**2 # area of the circle
herman_circle = 2 * r**2 # area of the circle in taxicab geometry

print("%.6f" % circle)
print("%.6f" % herman_circle)