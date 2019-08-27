# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:40:06 2017

@author: vsankar.la
"""
"""
Reinforcement
"""
#Exer 1
def is_multiple(n,m):
    try:
         #return True if m%n==0 else False
         return m%n==0
    except Exception as e:
        return False
#Exer 2
def is_Even(k):
    try:
         if k==0:
             return True
         elif k==1:
             return False
         else:
             return is_Even(k-2)
    except Exception as e:
        return False
  
def is_EvenHighStanderds(n):
    return not n & 1 # provided n is an integer
#Exer 3

def minMax(lis):
    a = b = lis[0]
    for i in lis:
        a = a if a < i else i
        b = b if b > i else i
    print(a,b)
    
#Exer 4

def squares(n):
    if n>0:
        if n-1==1:
            return 1
        else:
            return (n-1)*(n-1) + squares(n-1)
    else:
        return 0

#Exer 5
sum([y*y for y in range(1,12)])

#Exer 6
def oddSquares(n):
    if n>0:
        if n-1==1:
            return 1
        else:
            if (n-1)%2==1:
                return (n-1)*(n-1) + oddSquares(n-1)
            else:
                return oddSquares(n-1)
    else:
        return 0
#Exer 7

sum([y*y for y in range(1,8) if y%2==1]) # or If y & 1

        
#Exer 8
#j=len(x)+k


#Exer 9
#for x in range(50,90,10):
    #print(x)

#Exer 10

#for x in range(8,-10,-2):
    #print(x)

#Exer 11

def twoFactors(n):
    x = 1
    while x <=n:
        yield x
        x = 2*x      
    
print([x for x in twoFactors(256)])    
print([2**x for x in range(9)])        
#%%
#Exer 18

def sumOfDouble(n):
    x,y=0,2
    while y<=n:
        x+=y
        y+=2
        yield x

print([x for x in sumOfDouble(18)])
print([a*a+a for a in range(10)])
    

print([chr(x) for x in range(97,123)])