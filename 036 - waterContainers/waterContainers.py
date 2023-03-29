# File        :   waterContainers.py
# Version     :   1.0.0
# Description :   Solution to the waterContainers problem
#                
# Date:       :   Mar 28, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container 
# contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Explanation: 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

def maxArea(h):
    # Total containers:
    totalContainers = len(h)

    # Set indices:
    aIndex = 0
    bIndex = totalContainers - 1

    # The results arestored here:
    currentMaxArea = 0
    bestContainers = [0]

    processedContainers = 1
    searchArea = True

    # While traversing through the containers
    # array, looking for the max area:
    while (searchArea):

        # Get containers at indices:
        aSide = h[aIndex] # Container at the left
        bSide = h[bIndex] # Container at the right

        # Get rectangle dimensions:
        currentBase = abs(bIndex - aIndex)
        currentHeight = min(aSide, bSide)

        # Get Area
        currentArea = currentBase * currentHeight

        # Check if current max:
        if (currentArea > currentMaxArea):
            # Store max obtained so far:
            currentMaxArea = currentArea
            bestContainers[0] = (aIndex, bIndex)

        # Increase processed containers:
        processedContainers += 1

        # Check if all containers were already 
        # traversed:
        if (processedContainers >= totalContainers):
            searchArea = False
        else:
            # Search new containers:
            if (aSide > bSide):
                # a is bigger, change b:
                bIndex = bIndex - 1
            else:
                # b is bigger, change a:
                aIndex = aIndex + 1

    # Done:
    print(currentMaxArea, bestContainers)
    return currentMaxArea

# Test case:
h = [1,8,6,2,5,4,8,3,7]
a = maxArea(h)

print(a)
