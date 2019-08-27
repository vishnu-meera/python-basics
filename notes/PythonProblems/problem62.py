# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:51:24 2017

@author: vsankar.la
"""

import requests
#print(dir(requests))

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])