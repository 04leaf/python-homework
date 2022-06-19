# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:19:23 2020

@author: user
"""

import re

socialid = '''

身分證A223456789

阿花H123234789

小張的id h198723476

Happy new Year

12345 A543234567

A12398734567938

'''
i=re.compile(r"\w[1,2]\d{8}");
r=re.findall(i,socialid);
print(r);