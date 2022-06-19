# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:43:40 2022

@author: user
"""
t=int
x=int(input('請輸入x\n'))
y=int(input('請輸入y\n'))
if x>y:
    t=x
    x=y
    y=t
for i in range(x,0,-1):
    if x%i==0 and y%i==0:
        print('%d和%d的最大公因數是%d'%(x,y,i))
        print('%d和%d的最小公倍數是%d'%(x,y,x//i*y))
        break