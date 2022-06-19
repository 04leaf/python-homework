# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:35:24 2022

@author: user
"""

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    print(pos)
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix('123.exe'))