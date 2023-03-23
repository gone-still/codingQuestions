# File        :   pickingNumbers.py
# Version     :   1.5.0
# Description :   Solution to the pickingNumbers problem
               
# Date:       :   Feb 24, 2023
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

# The subarray can have multiple occurrences of
# the same item, test all the number against 
# themselves, duplicate the entries:
dictKeys = dictKeys + dictKeys

# Sort again, from small to large:
dictKeys.sort()

# Get total pairs:
totalPairs = len(dictKeys)
# Prepare subarray:
subArray = []
maxLength = 0

# Loop through the keys list, get a pair of
# entries, compute their absolute difference
# and maximum length:

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
    
    print((a,b,aCount,bCount,d,l))
    
    # Difference must be less than or equal to 1.
    # SubArray most be of maximum length:
    if (d <= 1):
        # Only same items can have distance of 0,
        # adjust subarray length to remove the duplicated
        # item count:
        if (d == 0):
            l = 0.5 * l   
        # If pair lenght > 0, you are testing two different
        # items and subarray length should not be adjusted:         
        if (l > maxLength): 
            maxLength = l     

# The practicing website gives wrong score if
# the result is not an integer (LOL):
maxLength = int(maxLength)
    
# Print the results:   
print(maxLength)
print(subArray)
