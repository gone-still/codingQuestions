# File        :   sortinBalls.py
# Version     :   1.0.0
# Description :   Solution to david's ball sorting problem
#                
# Date:       :   Feb 22, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# David has several containers, each with a number of balls in it. He has just enough containers to sort 
#each type  of ball he has into its own container. David wants to sort the balls using his sort method.

# David wants to perform some number of swap operations such that:

#  - Each container contains only balls of the same type.
#  - No two balls of the same type are located in different containers.

# Example:

# David has n=2 containers and 2 different types of balls, both of which are numbered from 0 to n-1=1. 
# In a single operation, David can swap two balls located in different containers.
# In this case, there is no way to have all green balls in one container and all red in the other using 
# only swap operations. 
# Return Impossible.

# Tip for the solution, which has nothing to do with programming. At all:

# The "tip" to note is that at least one container must be able to hold
# the largest amount of balls of one type. If this test fails, the sorting becomes
# impossible.


def organizingContainers(container):
    # Get container capacity:
    totalContainers = len(container)
    # Store max per row/column here:
    maxList = []
    
    # Process the matrix and then transpose it
    # Two times per matrix:
    for i in range(2):
        # The sum of all rows is stored here:
        sumList = []
        # Transpose on second iteration:
        if (i == 1):
            # Transpose the container:
            container = list(map(list, zip(*container)))
        # For each matrix row:
        for j in range(totalContainers):
            # Sum row by row:
            row = container[j]
            sumList.append(sum(row))
            
        # Get max per columns:    
        rowMax = max(sumList)
        # Store max:
        maxList.append(rowMax)   
    
    # The maximum count of balls of a type must match
    # the maximum capacity of at least one container: 
    outString = "Impossible"    
    if (maxList[0] == maxList[1]):
        outString = "Possible"
        
    return outString


# Test case:
data = [[0,2,1],
        [1,1,1],
        [2,0,0]]

# Get result
stringResult = organizingContainers(data)

# Set result:
print(stringResult)
