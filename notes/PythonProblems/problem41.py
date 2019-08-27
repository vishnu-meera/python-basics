# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:46:06 2017

@author: vsankar.la
"""
import string

try:
        
    def createAlphabetFile(filePath):
        file = open(filePath,'a')
        for _ in range(1,27):
            file.write(chr(96+_) + "\n")
        file.close()
        
    def createAlphabetFile_string(filePath):
        file = open(filePath,'a')
        for _ in string.ascii_lowercase:
            file.write(_ + "\n")
        file.close()
        
    createAlphabetFile("c:\\users\\vsankar\\desktop\\py\\text.txt")
    createAlphabetFile_string("c:\\users\\vsankar\\desktop\\py\\text.txt")
except Exception as e:
    print(e)