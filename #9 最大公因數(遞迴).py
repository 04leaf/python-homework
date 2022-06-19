# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:11:54 2020

@author: user
"""

def fun(a,b):
    if a%b==0:
        return b;
    else:
        return fun(b,a%b);
    
a,b=int(input()),int(input());
print(fun(a,b));