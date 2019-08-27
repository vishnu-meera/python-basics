# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:32:26 2017

@author: vsankar.la
"""

import requests
r = requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text.count("a")
print(text)