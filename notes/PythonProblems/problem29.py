# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:37:47 2017

@author: vsankar.la
"""
from math import pi

def partialyFilledSphereFormula(h,r):
    return (((4*pi*(r**3))/3)-((pi*h*h*(3*r-h))/3))


print(partialyFilledSphereFormula(2,10))


def foo(b=3,a=2):
    return a+b

x = foo()-1
       
c=1
def fee():
    c=2
    return c
c=3
print(fee())

def fii():
    global f
    f=1
    return f
fii()
print(f)