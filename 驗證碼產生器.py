# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:08:26 2022

@author: user
"""

import random
def generate_code(code_len=4):
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos=len(all_chars)-1
    code=''
    for i in range(code_len):
        index=random.randint(0,last_pos)
        code=code+all_chars[index]
    return code
print(generate_code(10))