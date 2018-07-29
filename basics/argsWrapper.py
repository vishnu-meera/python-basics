# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:03:57 2018

@author: Maalu
"""

def multipler10(number=2):
    return 10*number

def product10(x=2,y=3,z=4):
    return 10*x*y*z

def Wrapper(func,*args):
    print(args)
    return func(*args)
    
print(Wrapper(multipler10,10))
print(Wrapper(product10,2,3,4))

print(Wrapper(multipler10))
print(Wrapper(product10))