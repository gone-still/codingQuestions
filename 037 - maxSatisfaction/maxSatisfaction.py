# File        :   maxSatisfaction.py
# Version     :   1.0.0
# Description :   Solution to the maxSatisfaction problem
#                
# Date:       :   Mar 29, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# A chef has collected data on the satisfaction level of his n dishes. Chef can 
# cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish 
# including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain after 
# dishes preparation.

# Dishes can be prepared in any order and the chef can discard some dishes to get 
# this maximum value.

# Example 1:

# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14

# Explanation: After Removing the second and last dish, the maximum total like-time 
# coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.

def maxSatisfaction(inputList):
    # Sort the list:
    inputList.sort()

    # Base variables:
    listLength = len(inputList)
    totalSatisfaction = 0
    accumulator = 0

    # Loop through the list in reverse. Get current satisfaction value,
    # carry it over every iteration until the accumulated satisfaction is
    # negative. Additionally, sum-accumulate it during each iteration, this is
    # the total satisfaction level so far.
    for i in range(listLength - 1, -1, -1):
        currentSatisfaction = inputList[i]
        accumulator = accumulator + currentSatisfaction
        # Stop if satisfaction accumulator is negative:
        if (accumulator < 0):
            break
        # Accumulate each satisfaction value computed during
        # each iteration:
        totalSatisfaction = totalSatisfaction + accumulator

    # Done
    return totalSatisfaction


# Set the input array:
inputArray = [-10, -7, -2, -1, 0, 5, 10]
# Get satisfaction...
s = maxSatisfaction(inputArray)
print(s)
