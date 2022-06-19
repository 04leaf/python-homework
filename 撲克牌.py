# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:54:02 2020

@author: user
"""
import random
t=[]
u=[]
q=['黑桃','方塊','梅花','紅心']
for a in range(4):
    for b in range(13):
        u.append(str(q[a])+str(b+1))
for i in range(0,52,1):
    t.append(u[random.randint(0,51-i)])
    u.remove(t[i])
print(t)