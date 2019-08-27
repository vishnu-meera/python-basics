# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:35:17 2017

@author: vsankar.la
"""
import pprint
d = {
    'a':[x for x in range(1,11)],
    'b':[x for x in range(11,21)],
    'c':[x for x in range(21,31)]}

pprint.pprint(d)
print(d['b'][2])

for _ in d.keys():
    print(_, " has value ", d[_])

for key,value in d.items():
    print(key, " has value ", value)