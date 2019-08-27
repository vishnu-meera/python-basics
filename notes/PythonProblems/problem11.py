# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:52:54 2017

@author: vsankar.la
"""
my_range = [_ for _ in range(1,21)]
my_range2 = range(1,21)
print(my_range)
print(list(my_range2))
my_range_10 = [_*10 for _ in range(1,21)]
print(my_range_10)
my_range_str = [str(_) for _ in range(1,21)]
print(my_range_str)
print(list(map(str,my_range)))
