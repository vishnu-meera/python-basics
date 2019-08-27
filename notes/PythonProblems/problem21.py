# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:18:31 2017

@author: vsankar.la
"""

d = {"a": 1, "b": 2, "c": 3}
print({k:v for (k,v) in d.items() if v<=1})
