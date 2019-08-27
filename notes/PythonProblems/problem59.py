# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:23:24 2017

@author: vsankar.la
"""

try:
    a = [1,2,3]
    for _ in range(0,len(a)):
        print("Item %s have index %s"%(a[_],_))
        
    for index, item in enumerate(a):
        print("Item %s have index %s"%(item,index))
        
    #while True:
        #print("Hello")

except Exception as e:
    print(e)
        