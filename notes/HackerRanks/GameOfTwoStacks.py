#!/bin/python3

import sys
g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    
    sum,i,j,res=0,0,0,0
    while i<len(a) and sum+a[i]<=x:
        sum = sum + a[i]
        i = i + 1
        
    res = i
   
    while i>=0:
        while j<len(b) and sum+b[j]<=x:
            sum = sum + b[j]
            j = j + 1
           
        res = i + j if i + j> res else res
        i = i-1
        sum = sum - a[i]
        
    print(res)