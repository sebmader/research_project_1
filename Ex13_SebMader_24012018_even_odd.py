#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:26:39 2018

@author: Sebastian Mader (S3503704)
"""

# declare a default string of numbers
StringNum = "1,2,3,4,5,6,7,8,9"
# ask for the input of a string of numbers
StringNum = raw_input("Please enter a string of numbers separated by commas:\n")
# split the single string into a list of strings
StringNum = StringNum.split(',')
# convert the list elements into integers
StringNum = [int(Element) for Element in StringNum]
# declare empty lists for even and odd numbers
EvenList = []
OddList = []
# declare variables for mean values
EvenMean = 0.0
OddMean = 0.0
# loop through the list of all numbers
for Num in StringNum:
    # if it is odd (devided by 2 leaves remainder 1 (= true))
    if Num % 2:
        OddList.append(Num) # add element to list of odds
        OddMean += Num      # add element to sum of all odds
    # if it is even (devided by 2 leaves remainder 0 (=false))
    else:
        EvenList.append(Num) # add element to list of evens
        EvenMean += Num      # add element to sum of all evens

# devide the sums by the length of the lists --> mean
EvenMean /= len(EvenList)
OddMean /= len(OddList)

# print the results
print "List of all numbers: ", StringNum
print "List of even numbers: ", EvenList
print "   Mean value: %.3f" % (EvenMean)
print "List of odd numbers: ", OddList
print "   Mean value: %.3f" % (OddMean)