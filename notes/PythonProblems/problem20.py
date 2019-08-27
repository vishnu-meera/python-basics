# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:34:08 2017

@author: vsankar.la
"""

d = {"a": 1, "b": 2, "c": 3}
summ=0
for x in d.keys():
    summ+=d[x]
print(summ)

print(sum(d.values()))