# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:48:59 2019

@author: nebelgrau
"""

# DRM Messages

encrypted = input()

first_half = encrypted[:int(len(encrypted)/2)]  # split the encrypted message in two halves
second_half = encrypted[int(len(encrypted)/2):]

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # list of uppercase letters

code = dict(zip(letters, range(26))) # make a dictionary letter:number (can be skipped)

letters_list = [_ for _ in letters] # list of letters

def rotate(half): 

    rotation = 0

    for letter in half:
        rotation += code[letter] # rotation is a sum of indexes of letters

    new_letters = []
    
    for letter in half:
        new_index = (letters_list.index(letter) + rotation)%26 
        # letters are moved to the right by rotation amount
        # if they go over 26, it starts from 0
        new_letters.append(letters[new_index])

    return(new_letters)

new_letters_1st = rotate(first_half)
new_letters_2nd = rotate(second_half)

final_letters = []

for i in range(len(new_letters_1st)):
    index_1st = letters_list.index(new_letters_1st[i]) # get the index of i letter in the first list
    index_2nd = letters_list.index(new_letters_2nd[i]) # get the index of i letter in the second list
    new_index_1st = (index_1st + index_2nd)%26 # first moved by amount of second
    final_letters.append(letters[new_index_1st])

print(''.join(final_letters))