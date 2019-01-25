#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:55:17 2019

@author: nebelgrau
"""

# Run-Length Encoding, Run!

def encoder(message):
    '''scans the message, looking for groups of the same characters
    when it finds one, saves the last count, e.g. 4 if there are four 
    characters'''
    
    encoded = []
    n_count = 1

    for n in range(1, len(message)):
        if message[n] == message[n-1]:
            n_count += 1
        else:
            encoded.append((message[n-1], n_count))
            n_count = 1
    
    # it won't get the last character group, hence the check:
    
    len_check = 0
    for t in encoded:
        len_check += t[1]
    
    # get the last group
    encoded.append((message[-1], len(message)-len_check))
    
    encoded_message = ''

    for pair in encoded:
        encoded_message = encoded_message + pair[0] + str(pair[1])

    return(encoded_message)

def decoder(message):

    '''detects integer i, concatenates i previous characters, 
    e.g. x3 becomes xxx'''
    
    decoded = []
    for n in range(len(message)):
        try:
            number = int(message[n])
            decoded.append(message[n-1]*number)
        except:
            pass

    return(''.join(decoded))

flag, message = input().split()

# if the first character is 'D', then do the decoding, if 'E' encoding

if flag == 'D':
    print(decoder(message))
elif flag == 'E':
    print(encoder(message))
else:
    pass