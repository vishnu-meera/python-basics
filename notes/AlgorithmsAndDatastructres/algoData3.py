# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:55:46 2017

@author: vsankar.la
"""

class Adder(object):
    def __init__(self, num=0):
        self.num = num
        
    def __iadd__(self, other):
        print("in __iadd__", other)
        self.num  = self.num + other
        return self.num

a = Adder(2)
print(a)
a += 3
print(a)

b=2
b += 2
print(b)