# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:28:30 2017

@author: vsankar.la
"""#filepath
import string
try:
     def writeTwoAlphabet(filepath):
         file = open(filepath,'w')
         for _ in range(0,len(string.ascii_lowercase),2):
             i,j=string.ascii_lowercase[_:_+2]
             print(i+j)
             file.write(i+j+"\n")
         file.close()
     writeTwoAlphabet("C:\\Users\\vsankar\\Desktop\\PY\\text2.txt")    
     
     with open("C:\\Users\\vsankar\\Desktop\\PY\\text3.txt",'w') as file:
         for l1,l2,l3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
             file.write(l1+l2+l3+"\n")
    
except Exception as e:
    print(e)