# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:38:06 2020

@author: user
"""
s=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
for i in range(len(s[0])):
    for j in range(len(s[1])):
        print(i+1,'*',j+1,'=',s[0][i]*s[1][j])
