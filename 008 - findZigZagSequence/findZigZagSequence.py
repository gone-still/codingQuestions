# File        :   findZigZagSequence.py
# Version     :   1.0.0
# Description :   Solution to the findZigZagSequence problem
#                
# Date:       :   Feb 06, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of n distinct integers, transform the array into a zig zag 
# sequence by permuting the array elements. A sequence will be called a 
# zig zag sequence if the firstk elements in the sequence are in increasing 
# order and  the last k elements are in decreasing order, where k = (n + 1) / 2. 

# You need to find the lexicographically smallest zig zag sequence of the given array.

# Example:

# a = [2, 3, 5, 1, 4]

# Now if we permute the array as [1, 4, 5, 3, 2], the result is a zig zag sequence.

def findZigZagSequence(a, n):

    # Sort from smallest to largest
    a.sort()
    
    # Get middle of the list:
    mid = ((n + 1) // 2)

    # Switch middle for last, and last for middle:
    m = a[mid-1]
    l = a[n - 1]
    a[mid-1], a[n - 1] = a[n - 1], a[mid-1]

    # Set start and end indices:
    st = mid # starts at middle + 1
    ed = n - 2 # starts at end - 2
    
    # While end index is greater than the start
    # index, keep flipping the elements:
    while (st <= ed):
        
        # Flip elements:
        x = a[st]
        y = a[ed]
        a[st], a[ed] = a[ed], a[st]

        # Increase start, decrease end indices
        st = st + 1
        ed = ed - 1

    # Print the ordered sequence:
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

# Test case entry:
test_cases = 1
for cs in range(test_cases):
    n = 7
    a = [1, 2, 3, 4, 5, 6, 7]
    findZigZagSequence(a, n)
