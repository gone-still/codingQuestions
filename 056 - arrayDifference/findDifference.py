# File        :   findDifference.py
# Version     :   1.0.0
# Description :   Solution to the findDifference problem
#                
# Date:       :   Jun 02, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]

# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]

# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].


def findDifference(nums1, nums2):

    numDict = {}
    nums1Length = len(nums1)

    # Create the counter of numbers
    # in nums1:
    for i in range(nums1Length):
        currentNum = nums1[i]
        if currentNum not in numDict:
            numDict[currentNum] = 1

    # Check for repeated numbers
    # in nums2:
    nums2Length = len(nums2)
    list2 = []
    for i in range(nums2Length):
        currentNum = nums2[i]
        if currentNum not in numDict:
            if currentNum not in list2:
                list2.append(currentNum)
        else:
            numDict[currentNum] = 0

    # Build list1 with numbers on nums1
    # but not in nums2:
    list1 = []
    for key in numDict:
        value = numDict[key]
        if value == 1:
            list1.append(key)

    result = [list1, list2]
    return result



# Test case:
nums1 = [1,2,3]
nums2 = [2,4,6]
out = findDifference(nums1, nums2)
print("Out:", out)