# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:39:26 2017

@author: vsankar.la
"""
import time
try:
    i=0
    while True:
        print("Hello")
        i+=1
        if i>3:
            print("End of the loop")
            break
        time.sleep(i)


except Exception as e:
    print(e)