# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:36:51 2017

@author: vsankar.la
"""

class myStack:
    
    def __init__(self):
        self.container = []
    
    def push(self,element):
        self.container.append(element)
    
    def pop(self):
        try:
            return self.container.pop()
        except Exception as e:
            return e
        
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.container == []

    def top(self):
        try:
            return self.container[-1]
        except Exception as e:
            return e

newS =  myStack()
newS.push(1)
newS.push(3)
newS.push(8)
print(newS.isEmpty())
print(newS.size())
print(newS.pop())
print(newS.size())
print(newS.isEmpty())
print(newS.top())
newS.pop()
newS.pop()
newS.pop()
