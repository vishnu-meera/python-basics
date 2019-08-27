# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:55:04 2017

@author: vsankar.la
"""

def InsertionSort(list1):
    for j in range(1, len(list1)):
        card = list1[j]
        i=j-1
        while (i>=0 ) and (list1[i]>card):
            list1[i+1]=list1[i]
            i=i-1
            print("while ",list1)
        list1[i+1]=card
        print("for ",list1)     
    print(list1)
    
#InsertionSort([1,8,4,3,6,5,7,0,2])

InsertionSort([4,3,2,1,0])

        
        