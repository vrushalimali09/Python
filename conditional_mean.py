# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:49:17 2020

@author: Vrushali
"""

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

student_greads = {"John": 4.5, "Rohn": 5.6, "Smith": 7.8}
monday_temp = [45.6,67.8,34.5]

print(mean(monday_temp))

    