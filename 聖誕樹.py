# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 00:11:09 2022

@author: user
"""
row =int(input())
for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()
    
for i in range(row):
    for j in range(row):
        if j <  row-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()