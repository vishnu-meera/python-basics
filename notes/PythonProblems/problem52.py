# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:33:52 2017

@author: vsankar.la
"""

import json
import pprint
try:
    with open ("C:\\Users\\vsankar\\Desktop\PY\\Newfolder\\dictionary.json", 'r') as file:
        dic = json.load(file)
        #dic = json.loads(file.read())
        file.close()
    pprint.pprint(dic)
except Exception as e:
    print(e)
