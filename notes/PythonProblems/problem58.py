# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:48:31 2017

@author: vsankar.la
"""

import json
import pprint
try:
    with open ("C:\\Users\\vsankar\\Desktop\PY\\Newfolder\\dictionary.json", 'r+') as file:
        dic = json.loads(file.read())
        pprint.pprint(dic)
        dic["employees"].append({'firstName': 'Meera', 'lastName': 'Raveendran'})
        file.seek(0)
        json.dump(dic,file,indent=4,sort_keys=True)
        file.close()
except Exception as e:
    print(e)