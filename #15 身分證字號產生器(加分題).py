# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:30:55 2020

@author: user
"""

import random
pre={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
head="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
head=head[random.randint(0,25)];
center=random.randint(10000000,29999999);
center=str(center);
center=center[0:8];
end=int(center[0])*8+int(center[1])*7+int(center[2])*6+int(center[3])*5+int(center[4])*4+int(center[5])*3+int(center[6])*2+int(center[7])*1;
end=end+pre[head]//10+pre[head]%10*9;
end=10-end%10;
if end==10:
    end=0;
end=str(end);
N=head+center+end;
print(N);