# File        :   threeSum.py
# Version     :   1.0.0
# Description :   Solution to the threeSum problem
#                
# Date:       :   Jun 01, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


def threeSum(nums):
    # Sort nums:
    nums.sort()
    # Get total items:
    totalNumbers = len(nums)
    # Found (unique) triplets are stored here:
    tripletDict = {}

    for i in range(totalNumbers):
        # Set current target:
        currentNum = nums[i]
        currentTarget = -currentNum

        # Set left and right:
        leftIndex = i + 1
        rightIndex = totalNumbers - 1

        # Search for combinations:
        while leftIndex < rightIndex:

            # Skip target:
            cond1 = leftIndex == i
            cond2 = rightIndex == i

            # Check conditions to skip target:
            if cond1 or cond2:
                if cond1:
                    leftIndex += 1
                else:
                    rightIndex -= 1

            else:

                # Get left and right:
                left = nums[leftIndex]
                right = nums[rightIndex]

                # Compute current sum:
                currentSum = left + right

                # If current sum is larger than current target,
                # move right towards left:
                if currentSum > currentTarget:
                    rightIndex -= 1
                else:
                    # Gotta move left, but first check if sum == target:
                    if currentSum == currentTarget:
                        # Create the triplet list:
                        tempList = [currentNum, left, right]
                        tempList.sort()
                        # List to string (to be hashable):
                        currentKey = str(tempList)
                        # Check if key is unique:
                        if currentKey not in tripletDict:
                            # Store, along indices:
                            tripletDict[currentKey] = [i, leftIndex, rightIndex]
                        rightIndex -= 1

                    # Move left towards right:
                    leftIndex += 1

    # Get list of triplets:
    result = []
    for key in tripletDict:
        # string to list:
        currentKey = eval(key)
        result.append(currentKey)

    # Done:
    return result


# Test case:
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
out = threeSum(nums)
print("Out:", out)
