# File        :   pickingNumbers.py
# Version     :   1.0.0
# Description :   Solution to the pickingNumbers problem
#                
# Date:       :   Feb 23, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of integers, find the longest subarray where the absolute difference 
# between any two elements is less than or equal to 1.

# Example:
# a = [1,1,2,2,4,4,5,5,5]

# There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. 
# The maximum length subarray has 5 elements.

from collections import Counter

data = [4, 6, 5, 3, 3, 1]

# Get a count of the items:
countDict = Counter(data)
# Sort counter by keys, from smallest to largest:
countDict = dict(sorted(countDict.items()))
# Get keys list:
dictKeys = list(countDict.keys())

# Loop through the keys list, geta pair of
# entries, compute their absolute difference
# and maximum length:

maxLength = 0
subArray = []

for i in range(len(dictKeys)-1):
    
    # Get a pair:
    a = dictKeys[i]
    b = dictKeys[i+1]
    
    # Compute absolute difference:
    d = abs(a-b)
    
    # Get entries counts:
    aCount = countDict[a]
    bCount = countDict[b]
    
    # Compute subarray length for
    # this pair:
    l = aCount + bCount
    
    # Difference must be less than or equal to 1.
    # SubArray most be of maximum length:
    if (d <= 1) and (l > maxLength):
        maxLength = l
        subArray = [a]*aCount + [b]*bCount
        
# Print the results:   
print(maxLength)
print(subArray)
