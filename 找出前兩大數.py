# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:48:45 2022

@author: user
"""

def max2(x):
    m1,m2=(x[0],x[1])if x[0]>x[1] else(x[1],x[0])
    for index in range(2,len(x)):
        if x[index]>m1:
            m2=m1
            m1=x[index]
        elif x[index]>m2:
            m2=x[index]
    return m1,m2
y=[54,54,24,34,97,64,52,1,21,133]
print(max2(y))