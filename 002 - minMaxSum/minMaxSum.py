# File        :   minMaxSum.py
# Version     :   1.0.0
# Description :   Solution to the minMaxSum problem
#                
# Date:       :   Feb 01, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four 
# of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated 
# long integers.

# Example: arr = [1,3,5,7,9]

# The minimum sum is: 1 + 3 + 5 + 7 = 16
# the maximum sum is: 3 + 5 + 7 + 9 = 24

# The function prints:
# 16 24


#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    
    # Order list from smallest to larger:
    orderedList = arr.sort()
    
    # Set cum sums:
    minSum = 0
    maxSum = 0
    
    totalItems = len(arr)
    
    # Extract the first and last items from
    # the list:
    for i in range(4):
        # Sum of smallest elements:
        minSum = arr[i] + minSum
        # Sum of largest elements:
        maxSum = arr[totalItems-(i+1)] + maxSum
    
    # Print results:
    print(str(minSum)+" "+str(maxSum))
        
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
