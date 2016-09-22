# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:04:49 2016

@author: jameslegros
"""

# Assume s is a string of characters

s = 'azcbobobegghakl'

#Length
length = len(s)

#String increment
i = 0

#Vowel count
count = 0

while (length > i):
    
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        count += 1
    
    i += 1
    

print ("Number of vowels: " + str(count))