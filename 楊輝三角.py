# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:14:43 2022

@author: user
"""

num = int(input('Number of rows: '))
yh = [[]] * num
for row in range(len(yh)):
    yh[row] = [None] * (row + 1)
    for col in range(len(yh[row])):
        if col == 0 or col == row:
            yh[row][col] = 1
        else:
            yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
        print(yh[row][col], end='\t')
    print()