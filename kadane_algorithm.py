# -*- coding: utf-8 -*-
"""
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
"""

def kadane(arr):
    max_ending=0
    max_so_far=0
    for i in range(len(arr)):
        max_ending=max_ending+arr[i]
        if max_ending<0:
            max_ending=0
        elif(max_ending>max_so_far):
            max_so_far=max_ending
    return max_so_far