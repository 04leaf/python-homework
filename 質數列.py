# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:23:43 2022

@author: user
"""

from math import sqrt

for j in range(2,100):
    A=j
    B=True
    for i in range(2,A):
        if A%i==0:
            B=False
            break
    if B and A !=1:
        print(A)