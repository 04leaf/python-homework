# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:21:56 2020

@author: user
"""
m=int(0);
def fun(a):
    print(a);
    global m
    m=m+1;
    if a!=1 and a%2==0:
        a=fun(a//2);
    if a!=1 and a%2!=0:
        a=fun(3*a+1);
    return m;
b=int(input());
print('有',fun(b),'個數字');
    
