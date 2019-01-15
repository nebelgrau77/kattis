# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:27:32 2019

@author: nebelgrau
"""

# Kemija

words = [_ for _ in input().split()] # split input into single words

new_words = []

for word in words:

    new_string = []
    position = 0

    while position < len(word): # iterate over letters in each word
        if word[position] in 'aeiou': # if the letter is a vowel
            new_string.append(word[position]) # add to the list of new letters 
            position = position + 3 # and skip the next two letters
        else:
            new_string.append(word[position]) 
            position = position + 1 # otherwise just move to the next letter
        
        
    print(''.join(new_string),end = ' ') # print the results in one line