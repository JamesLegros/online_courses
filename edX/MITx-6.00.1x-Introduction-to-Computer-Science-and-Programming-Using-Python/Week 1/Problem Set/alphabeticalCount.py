# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:25:19 2016

@author: jameslegros
"""

s = 'zyxwvutsrqponmlkjihgfedcba'

#Length
length = len(s)

#String increment
i = 1

#Letter count
count = 1

#Temp initialize
temp = 1

#longest
#longest = ''

#Position
p1=1
p2=1
while ((length) > i):
    
        

    if(s[i] >= s[i-1]) and (i+1==length) and (temp >= count):
        temp += 1        
        count = temp
        p2 = i+1   
    elif (s[i] >= s[i-1]):
        temp += 1
    elif (temp > count):
        count = temp
        p2 = i
        temp = 1   
    else:
        temp = 1
    
    i += 1
  

p1 = p2-count

print ("Longest substring in alphabetical order is: " + s[p1:p2])











