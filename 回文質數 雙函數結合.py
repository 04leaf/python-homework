# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:24:21 2022

@author: user
"""

def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True if num!=1 else False

def palindrome(num):
    temp=num
    total=0
    while temp>0:
        total=total*10+temp%10
        temp=temp//10
    return total==num

x=int(input('輸入x確認是否為回文質數'))
if palindrome(x) and prime(x):
    print(x,'是回文質數')
else:
    print(x,'不是回文質數')