# File        :   twoSum.py
# Version     :   1.0.0
# Description :   Solution to the twoSum problem
#                
# Date:       :   Mar 21, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the 
# same element twice.

# You can return the answer in any order.

# Example:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def twoSum(nums, target):

    # Get a dictionary from the number list
    # Items as keys, their indices (list containing duplicates) as value:
    numberDict = {}
    [numberDict.setdefault(v, []).append(i) for i, v in enumerate(nums)]

    # The out indices are stored here:
    outList = []

    totalNumbers = len(nums)

    # Loop through the list in reverse:
    for i in range(totalNumbers, -1, -1):

        # Get number from list:
        currentIndex = i - 1
        currentNumber = nums[currentIndex]

        # Get the missing number by calculating
        # the difference between the target and the
        # current number:
        numberDifference = target - currentNumber

        # Check if the needed number exists in the dictionary:
        if numberDifference in numberDict:

            # And check if it is different from current
            # number (just get the first item on the index list):
            targetIndex = numberDict[numberDifference][0]

            if (targetIndex != currentIndex):
                # Save indices to out list:
                outList.append(targetIndex)
                outList.append(currentIndex)
                # Break from loop:
                break

    # Done:
    return outList


# Test case entry:
nums = [2, 4, 11, 8, 3]
target = 6

outRes = twoSum(nums, target)
print(outRes)
