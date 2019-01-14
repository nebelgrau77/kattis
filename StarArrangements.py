# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:24:26 2019

@author: nebelgrau
"""

stars = int(input())

results = []

for n in range(2,int(stars/2)+2): # check for combinations (n, n-1)
    counter = 0
    amount = stars
    
    while amount > 0:
        if counter%2 == 0:
            amount -= n
            counter += 1            
        else:
            amount -= n-1
            counter += 1
            
    if amount == 0:
        results.append((n, n-1))
    
for n in range(2,int(stars/2)+1):    # check for combinations (n,n)
    amount = stars
    if amount%n == 0:
        results.append((n, n))

results.sort(key = lambda x: (x[0])) # sort the tuples

      
print("{}:".format(stars))
for result in results:
    print("{},{}".format(result[0], result[1]))