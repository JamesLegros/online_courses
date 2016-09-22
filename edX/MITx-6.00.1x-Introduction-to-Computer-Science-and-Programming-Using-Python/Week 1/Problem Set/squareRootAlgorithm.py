# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

print ("Finding the square root")
num = int(input("Input an integer: "))

err = float(input("Input an error: "))

while err > (num/10):
    print ('\nError is too large!')
    err = int(input("Please try again: "))

'''   
Algorithm
Find square root of num
Take an initial guess g,
if: g*g is close to num +/- err, good enough
else:   x = num/g
        num = (x+g)/2
'''

#Initial guess
g = 2

#Iteration counter
i = 1


while (abs(num-(g*g)) > err):
    x = num/g
    g = (x+g)/2
    i+=1
    
print ("The square root is: " + str(g))
print ("It took " + str(i) + " iterations to complete")