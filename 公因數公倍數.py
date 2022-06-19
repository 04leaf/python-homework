# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:43:40 2022

@author: user
"""
def gcd(x,y):
    t=int
    if x>y:
        t=x
        x=y
        y=t
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            return i
def lcm(x,y):
    return x*y//gcd(x,y)
    
x=int(input('請輸入x\n'))
y=int(input('請輸入y\n'))
print('%d和%d的最大公因數是%d'%(x,y,gcd(x,y)))
print('%d和%d的最小公倍數是%d'%(x,y,lcm(x,y)))