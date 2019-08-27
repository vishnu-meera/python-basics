# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:42:12 2017

@author: vsankar.la
"""

import threading
import time

def myFunction():
    print("Start a thread\n")
    time.sleep(3)
    print("End a thread\n")
    
threads = []

for i in range(5):
    th = threading.Thread(target = myFunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()    
