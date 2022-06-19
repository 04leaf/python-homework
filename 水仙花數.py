# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:42:44 2022

@author: user
"""

for i in range(100,1000):
    low=i%10
    mid=i//10%10
    high=i//100
    if i==low**3+mid**3+high**3:
        print(i)