# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:12:40 2017

@author: vsankar.la
"""

a=[1,2,3]
b=(4,5,6)

def homologusSum(a,b):
    for _ in range(0,len(a)):
        print(a[_]+b[_])
        
#homologusSum(a,b)

def homologusZip(a,b):
    for i,j in zip(a,b):
        print(i+j)

homologusZip(a,b)