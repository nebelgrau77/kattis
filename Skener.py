# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:47:21 2019

@author: nebelgrau
"""

#Skener

R, C, Zr, Zc = map(int, input().split())

# read the original matrix
original_matrix = [] 
for n in range(R):
    row = [_ for _ in input()]
    
    original_matrix.append(row)
    
new_matrix = []

#recreate each row multiplying the elements as necessary
for row in original_matrix:
    new_row = []
    for element in row:
        
        for i in range(Zc):
            new_row.append(element)
    # recreate the new matrix repeating the new rows if necessary
    for i in range(Zr):
        new_matrix.append(new_row)
        
for row in new_matrix:
    print(''.join(row))