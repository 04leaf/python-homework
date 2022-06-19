# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:54:02 2022

@author: user
"""

X=int(input('輸入要求多少個費波納棄數列'))
T=0
A=1
B=1
if X==1:
    print('1')
elif X==2:
    print('1\n1')
else:
    print('1\n1')
    while X>2:
        X=X-1
        T=B
        B=B+A
        A=T
        print(B)
        
        