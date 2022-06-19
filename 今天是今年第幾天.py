# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:57:22 2022

@author: user
"""

def is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0
def which_day(year,month,date):
    days_of_month=[31,28,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31]
    total=0
    if is_leap_year(year): 
        for index in range(12,month+11):
            total=total+days_of_month[index]
    else:
        for index in range(month-1):
            total=total+days_of_month[index]
    return total+date
print(which_day(1980,12,31))
print(which_day(1981,12,31))