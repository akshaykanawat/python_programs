# -*- coding: utf-8 -*-
"""
Given an array of size n-1
 and given that there are numbers from 1 to n with one missing, the missing number is to be found.
"""

def missing(arr):
    n=len(arr)
    total=(n+1)*(n+2)//2
    sum_arr=sum(arr)
    remain=total-sum_arr
    print(remain)