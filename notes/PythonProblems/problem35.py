# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:45:21 2017

@author: vsankar.la
"""


def wordCount(string):
    string.replace(',',' ')
    print(string)
    return len(string.split(' '))

print(wordCount("the,quick,brown fox jumped over the lazy dog"))

file = open("C:\\Users\\vsankar\\Downloads\\words1.txt",'r')
print(wordCount(file.read()))
file.close()