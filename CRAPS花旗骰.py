# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:37:45 2022

@author: user
"""
from random import randint
money=1000

while money>0:
    print('總資產:',money)
    go=False
    while True:
        debt=int(input('請下注:'))
        if 0<debt<=money:
            break
    first =randint(1,6)+randint(1,6)
    print('玩家骰出了%d點數'% first)
    if first ==7 or first==11:
        print('玩家勝')
        money=money+debt
    elif first==2 or first==3 or first==12:
        print('庄家勝')
        money=money-debt
    else:
        go=True;
    while go:
        go=False
        current=randint(1,6)+randint(1,6)
        print('玩家骰出了%d點數'% current)
        if current==7:
            print('庄家勝')
            money=money-debt
        elif current==first:
            print('玩家勝')
            money=money+debt
        else:
            go=True
print('遊戲結束')