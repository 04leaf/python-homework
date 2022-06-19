# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:32:51 2020

@author: user
"""

a=int(input())
b=int(input())
c=int(input())

if a+b>c:
    if a*a+b*b<c*c:
        if a==b or b==c or c==a:
            print("三角形abc為等腰鈍角三角形")
        else:
            print("三角形abc為鈍角三角形")
    if a*a+b*b==c*c:
        if a==b or b==c or c==a:
            print("三角形abc為等腰直角三角形")
        else:
            print("三角形abc為直角三角形")
    if a*a+b*b>c*c:
        if a==b or b==c or c==a:
            print("三角形abc為等腰銳角三角形")
        else:
            print("三角形abc為銳角三角形")
else:
    print("abc不是三角形")