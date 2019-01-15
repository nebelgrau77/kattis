# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:31:55 2019

@author: nebelgrau
"""

# Hanging Out on the Terrace

limit, events = map(int, input().split())

party = 0
left = 0

for event in range(events):
    descr, group = input().split()
    group = int(group)
    if descr == 'leave':
        party -= group
    else:
        if party + group <= limit:
            party += group
        else:
            left += 1

print(left)