# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:36:06 2017

@author: vsankar.la
"""


a=['1',1,'1',2,2,1,'3']
b=[]
for _ in a:
    if(_ not in b):
        b.append(_)

print(b)
print(list(set(a)))