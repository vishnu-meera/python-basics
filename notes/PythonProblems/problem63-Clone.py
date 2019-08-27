# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:05:27 2017

@author: vsankar.la
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.pythonhow.com/data/universe.txt")
soup = BeautifulSoup(response.text)
print(soup.prettify())
