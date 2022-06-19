# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:23:43 2022

@author: user
"""

from math import sqrt

A=int(input('請輸入數字判斷質數\n'))
B=True
for i in range(2,A):
    if A%i==0:
        B=False
        break
if B and A !=1:
    print(A,'是質數')
else:
    print(A,'不是質數')