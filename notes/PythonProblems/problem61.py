# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:53:10 2017

@author: vsankar.la
"""
try:
    d    = dict(weather = "clima", earth = "terra", rain = "chuva")
    
    def askUser():
        key = str(input("Enter word: "))
        return key.strip().lower()
        
    def vocabulary(word):
        try:
            return (d[word])
        except KeyError as key:
            return "Not such word in the dictionary"
    
    print(vocabulary(askUser()))
    
except Exception as e:
    print(e)