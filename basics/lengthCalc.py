# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:24:50 2018

@author: Maalu
"""

def calculateLength(stringValue):
    if isinstance(stringValue,str):#or type(stringvalue)==str
        return len(stringValue)
    elif type(stringValue)==float:
        return "Sorry floats don't have length"
    else:
        return "Sorry integers don't have length"
    
print(calculateLength(100))
print(calculateLength(input("Enter some string: ")))