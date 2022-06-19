# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:37:40 2020

@author: user
"""
import random
student={'A':{'math':random.randint(0,100),'english':random.randint(0,100),'physical':random.randint(0,100)},'B':{'math':random.randint(0,100),'english':random.randint(0,100),'physical':random.randint(0,100)},'C':{'math':random.randint(0,100),'english':random.randint(0,100),'physical':random.randint(0,100)}};
for i,j in student.items():
    t=0;
    for k in j.values():
        t=t+k;
    student[i]['total']=t;
for a,b in student.items():
    ranki=1;
    for c,d in student.items():
        if b['total']<d['total']:
            ranki=ranki+1;
    student[a]['rank']=ranki;
for q,w in student.items():
    print('學生',q,'分數為:數學',w['math'],'分,英文',w['english'],'分,物理',w['physical'],'分')
    print('總分為',w['total'],'分,名次為',w['rank'],'名');


    