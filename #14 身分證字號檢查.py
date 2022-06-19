# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:29:02 2020

@author: user
"""
pre={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
id="A123456789";
id_pre=pre[id[0]];
x=id_pre//10+id_pre%10*9+int(id[1])*8+int(id[2])*7+int(id[3])*6+int(id[4])*5+int(id[5])*4+int(id[6])*3+int(id[7])*2+int(id[8])*1;
x=x%10;
print(x);
if int(id[9])==10-x:
    print("符合");
else:
    print("不符合");