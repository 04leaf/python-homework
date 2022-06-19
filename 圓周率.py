# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:59:27 2020

@author: user
"""
import random
p=0
n=int(input())
N=n*n
A=0
for i in range(0,N):
    x,y=random.randint(0,n),random.randint(0,n)
    A=A+1
    if x*x+y*y<=N:
        p=p+1
    if A%(N/100)==0:
        print(A/n,"%")
p=p*4/N
print(p)