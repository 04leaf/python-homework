# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:47:42 2022

@author: user
"""
import os
import time

content = '北京欢迎你为你开天辟地…………'
while True:
        # 清理屏幕上的输
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]