# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:47:20 2022

@author: user
"""

for i in range(4,10001):
    X=0
    for j in range(1,i//2+1):

        if i%j==0:
            X=X+j
    if X==i:
        print(X)
print('done')