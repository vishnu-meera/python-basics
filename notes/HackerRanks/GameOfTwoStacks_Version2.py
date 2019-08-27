#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    
    sum,count=0,0
    while len(a) > 0 and len(b) >0:           
        sum =sum + (a.pop(0) if(a[0]<b[0]) else b.pop(0))
        if sum > x :
            break
        count = count +1
    print(count)