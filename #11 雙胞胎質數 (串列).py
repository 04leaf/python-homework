# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:28:49 2020

@author: user
"""
t=[]
def k(k):
    for j in range(2,k-1,1):
        if k%j==0:
            return 0;
            break;
    return 1;
for i in range(2,10001,1):
    if k(i)==1:
        t.append(i)
for j in range(len(t)):
    if k(t[j]) and k(t[j]+2)==1:
        print('[',t[j],',',t[j]+2,']')