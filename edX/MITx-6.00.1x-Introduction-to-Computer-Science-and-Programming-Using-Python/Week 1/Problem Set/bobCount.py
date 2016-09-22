# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:16:46 2016

@author: jameslegros
"""

s = 'bobobobobobobobobob'

#Length
length = len(s)

#String increment
i = 0

#Vowel count
count = 0

while ((length-2) > i):
    
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
    
    i += 1
    

print ("Number of times bob occurs is: " + str(count))