# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:54:02 2018

@author: Maalu
"""
numbers = [1, 2, 3]
def listtofile(filename,numbers):
    if type(numbers)==list:
        myfile = open(filename,"a")
        [myfile.write(str(i)+"\n") for i in numbers]
        myfile.close()
    else:
        print("second argument should be a list")
listtofile("numbers.txt",numbers)
    
    