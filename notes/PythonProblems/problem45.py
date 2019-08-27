# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:51:22 2017

@author: vsankar.la
"""
import string
#for _ in range(1,27):
for letter in string.ascii_letters:
    filename = "C:\\Users\\vsankar\\Desktop\\PY\\Newfolder\\"+letter+".txt"
    file = open(filename,'w')
    file.write(letter)
    file.close()