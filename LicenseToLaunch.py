#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:59:05 2019

@author: nebelgrau
"""

# License to Launch

license = int(input())
debris = [int(x) for x in input().split()]
days_with_license = debris[:license]
best_day = days_with_license.index(min(days_with_license))

print(best_day)
