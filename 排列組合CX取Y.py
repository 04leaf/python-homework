# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:12:03 2022

@author: user
"""

def fac(num):
    result=1
    for n in range(1,num+1):
        result=result*n
    return result

X=int(input())
Y=int(input())
print(fac(X)//fac(Y)//fac(X-Y))