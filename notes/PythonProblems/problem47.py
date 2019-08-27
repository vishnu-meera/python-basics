# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:00:00 2017

@author: vsankar.la
"""
import glob

try:
    files = glob.glob("C:\\Users\\vsankar\\Desktop\\PY\\Newfolder\*.txt")
    letter = []  
    for file in files:
        with open(file,'r') as f:
            letter.append(f.read().strip("\n"))
            f.close()
    print(letter)
except Exception as e:
    print(e)