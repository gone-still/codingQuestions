# File        :   binarySearch.py
# Version     :   1.0.0
# Description :   Iterative implementation of binary search
#
# Date:       :   Mar 22, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Implements binary search. Gets the index of a target item in
# an ordered array.

def binarySearch(inputArray, target):
    # Get the array size:
    arraySize = len(inputArray)

    # Set the initial search indices:
    startIndex = 0
    endIndex = arraySize - 1

    # Out index at -1:
    index = -1
    pastIndex = -1

    iterationsCounter = 0
    # Stop flag:
    searchIndex = True

    # Run the algorithm while the target hasn't been
    # found:
    while searchIndex:

        # Compute middle index and get middle item:
        middleIndex = startIndex + (endIndex - startIndex) // 2
        middleItem = inputArray[middleIndex]

        # Check if target is in left:
        if (target < middleItem):
            # Compute new indices:
            endIndex = middleIndex - 1
            currentIndex = endIndex
        else:
            # Check if target is in right:
            if (target > middleItem):
                # Compute new indices:
                startIndex = middleIndex + 1
                currentIndex = startIndex
            else:
                # Got target:
                index = middleIndex
                searchIndex = False

        # Target not found stop condition:
        if (pastIndex == currentIndex):
            searchIndex = False

        # Current search index is now past index:
        pastIndex = currentIndex

        # Increase iterations counter:
        iterationsCounter += 1

    print("Got target: ", target, " at index: ", index, ", Iterations: ", iterationsCounter)
    return index


# Set the input array:
inputArray = [2, 5, 1, 25, 23, 15, 26, 12, 100, 27, 5, 20, 30, 35, 64, 3, 80]

# Sort the array from smallest to largest item:
inputArray.sort()
print(inputArray)

# Get the target element:
target = 30

# Get the index of the target element:
index = binarySearch(inputArray, target)
print(index)
