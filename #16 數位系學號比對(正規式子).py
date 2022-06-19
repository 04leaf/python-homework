# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:19:50 2020

@author: user
"""

import re;
student = '''

周阿花 XXT11020 18分 台中市

劉阿翔 ADT10502 90分 台北市

ADT10503

ADT10209

ADT9802

XYZ10508 ''';
s=re.findall('[A][D][T][1][0][0-8][0-9][0-9][0-9]',student);
print(s);