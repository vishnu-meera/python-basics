# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:45:29 2017

@author: vsankar.la
"""

def fibonocci(n):
    a,b,c=0,1,0
    
    while a<n:
        yield a
        c = a+b
        a = b
        b = c
for x in fibonocci(100):
    print(x)