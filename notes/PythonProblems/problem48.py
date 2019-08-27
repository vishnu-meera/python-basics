# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:15:01 2017

@author: vsankar.la
"""

import glob

try:
    files = glob.glob("c:\\users\\vsankar\\desktop\\PY\\newfolder\\*.txt")
    letters = []
    py = 'python'
    for file in files:
        with open(file,'r') as f:
            alpha = f.read().strip("\n").lower()
            if alpha in py:
                letters.append(alpha)
    print(letters)
    
except Exception as e:
    print(e)