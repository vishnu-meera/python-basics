# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:23:51 2018

@author: Maalu
"""

def celsiusToFahrenheit(celsius,coef=1.8):
    if celsius < -273.15:
        return "The temperature doesn't make any sense"
    return round(celsius*coef+32,2)

def fahrenheitToCelsius(fahrenheit,coef=.56):
    return round((fahrenheit-32)*coef,2)

#print(celsiusToFahrenheit(31))
#print(fahrenheitToCelsius(90))
temperatures=[10,-20,-289,100]
for c in temperatures:
    print(celsiusToFahrenheit(c))