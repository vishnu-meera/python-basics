# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:31:04 2017

@author: vsankar.la
"""

def factors(n):
    k=1
    while k*k < n:
        if n%k==0:
            yield k
            yield n//k
        k+=1
    if k*k == n:
        yield k

factor = [x for x in factors(100)]
print(factor)

square = [y*y for y in range(10)]
print(square)

total = sum(k for k in range(1,101))
print(total)

data = 2,3,4,5,6
print(data)
a,b,c,d = range(7,11)
print(a,b,c,d)

a, b = divmod(10,3)
print(a,b)
for x, y in [ (7, 2), (5, 8), (6, 4) ]:
    print(x,y)