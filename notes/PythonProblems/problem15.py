# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:25:58 2017

@author: vsankar.la
"""

d = {'a':1,'b':2}
print(d)

print(d['b'])
print(d['a'] + d['b'])
d.setdefault('c',3)
print(d)
d["c"]=4
print(d)
