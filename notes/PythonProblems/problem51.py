# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:47:34 2017

@author: vsankar.la
"""
import pprint
import json
try:
    print(type("hey".replace("ey","i")[-1]))
    vishnu = "vishnu"
    print("your first name is %s and sceond name is %s" % (vishnu ,vishnu))
    
    d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                    {"firstName": "Anna", "lastName": "Smith"},
                    {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
              {"firstName": "Jessy", "lastName": "Petter"}]}
    print(d["employees"][1]["lastName"])
    d["employees"][1]["lastName"] = "Smooth"
    print(d)
    d["employees"].append({"firstName": "vishnu", "lastName": "sankar"})
    pprint.pprint(d)
    
    with open("C:\\Users\\vsankar\\Desktop\\PY\\Newfolder\\dictionary.json",'w') as file:
        json.dump(d,file,indent=4,sort_keys=True)

except Exception as e:
    print(e)