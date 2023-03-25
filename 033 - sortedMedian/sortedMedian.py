# File        :   sortedMedian.py
# Version     :   1.0.0
# Description :   Solution to the sortedMedian problem
               
# Date:       :   Mar 24, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
# median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


def computeMedian(nums1, nums2):

    # IndimergedArrayidual lengths:
    length1 = len(nums1)
    length2 = len(nums2)

    # Total Length
    totalLength = length1 + length2

    # Array indices:
    i = 0
    j = 0

    # Merged array:
    mergedArray = []

    # Sort and merge:
    while ((i < length1) and (j < length2)):
        # Get both elements:
        a = nums1[i]
        b = nums2[j]
        # Check if item from first array
        # is smaller:
        if (a < b):
            mergedArray.append(a)
            i += 1
        # Check if item from second array
        # is smaller:
        else:
            mergedArray.append(b)
            j += 1

    # One side remains with numbers:
    # Check first array:
    while (i < length1):
        a = nums1[i]
        mergedArray.append(a)
        i += 1

    # Check second array:
    while (j < length2):
        b = nums2[j]
        mergedArray.append(b)
        j += 1

    print(mergedArray)

    # Get center index:
    middleIndex = totalLength // 2
    if (totalLength % 2 == 0):
        # EmergedArrayen:
        median = (mergedArray[middleIndex - 1] + mergedArray[middleIndex]) / 2.0
    else:
        # Odd:
        median = mergedArray[middleIndex]

    return median


# Test case:
nums1 = [1, 3]
nums2 = [2, 4, 7]

median = computeMedian(nums1, nums2)
print(median)
