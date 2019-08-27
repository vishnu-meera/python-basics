# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:25:01 2017

@author: vsankar.la
"""
import math

def wordCount(string):
    return len(string.replace(',',' ').split(' '))

file = open("C:\\Users\\vsankar\\Downloads\\words2.txt", 'r')
print(wordCount("hi,its me"))
print(wordCount(file.read()))
file.close()

print(math.sqrt(9))

print(math.cos(1))

