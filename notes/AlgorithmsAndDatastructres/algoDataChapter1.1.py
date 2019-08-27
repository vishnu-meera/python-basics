# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:33:33 2017

@author: vsankar.la
"""
#import random

def reverseTheList(lis):   
    print(lis)
    j,k=0,-1  
    while j<=len(lis)+k:
        lis[j],lis[k] = lis[k],lis[j]
        j+=1
        k+=-1
    print(lis)
    
#x = [1,2,4,5,6,7,8,9]
#y = [1,2,4,5,6,7,8]
#reverseTheList(x)
#reverseTheList(y)
#x =random.randrange(1,1000,1)
#print(x)

def myReverse(data):
    return [data[-(i+1)] for i in range(len(data))]
    
#print(myReverse([1, 2, 3, 4, 5]))
#print(myReverse([1]))

def is_SequnceDistinct(lis):
    return True if len(lis) == len(set(lis)) else False

#print(is_SequnceDistinct([1,2,4,5,8,9,0]))
#print(is_SequnceDistinct([1,2,3,4,5,6,2]))

def scale(data,factor):
    for i in range(len(data)):
        data[i]+=factor
    
def scaleMut(data,factor):
    for i in range(len(data)):
        data[i]=data[i] + factor

y = [1,2,3,4,5,6,2]


print(x,y)
scale(x,3)
print(x,y)


print("----------------------------")

a = [4,5,6]
b = a
print(a,b)
scaleMut(b,3)
print(a,b)


    