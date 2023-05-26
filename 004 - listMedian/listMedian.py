# File        :   listMedian.py
# Version     :   1.0.0
# Description :   Solution to the listMedian problem
#                
# Date:       :   Feb 03, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Compute the median of a list of
# numbers.

import math

# List of numbers:
numbersList = [1, 2, 3, 4]
# Get list size:
listSize = len(numbersList)
# Sort from smallest to largest:
numbersList.sort()

# Get middle (floored)
middle = listSize // 2

# Check list size:
if (listSize % 2 == 0):
    # If even, median is average between the two
    # middle elements:
    median = numbersList[middle] + numbersList[middle-1]
    median = median / 2
else:
    # If odd, median is just the central element:
    median = numbersList[middle]
    
# Done:
print(median)
