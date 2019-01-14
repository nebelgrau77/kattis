# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:46:24 2019

@author: nebelgrau
"""

# Reversed Binary Numbers

number = int(input())
digits = []
for i in range(32,-1,-1):            # conversion to binary
    digits.append(number//(2**i))    # e.g. n // 2**i 
    number = number%(2**i)           # what is left

digits_string = [str(_) for _ in digits] # binary digits

binary = int(''.join(digits_string)) # truncate zeros by joining digits and converting to integer

binary_digits = [_ for _ in str(binary)] # split into digits again

new_decimal = 0

for n in range(len(binary_digits)):
    new_decimal = new_decimal + int(binary_digits[n])*2**n
    
print(new_decimal)