# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:01:46 2020

@author: user
"""
def k(k):
    for j in range(2,k-1,1):
        if k%j==0:
            return 0;
            break;
    return 1;

def center(a):
    a=a*a*5+a*5+1
    return a;

s=int(0)
m=int(input('輸入數字m求小於等於m的中心十邊形質數:'))
while center(s)<=m:
    s=s+1;
    if k(center(s))==1:
            print(center(s));1