# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 01:05:36 2021

@author: Vrushali
"""

import time
import os

while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as file:
            print(file.read())
    else :
        print("File does not exists")
    time.sleep(10)
            