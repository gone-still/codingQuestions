# File        :   mergeSort.py
# Version     :   1.0.0
# Description :   Implementation of merge sort
#
# Date:       :   Mar 22, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0


def merge(leftArray, rightArray, array):
    # Sub arrays sizes:
    leftSize = len(leftArray)
    rightSize = len(rightArray)

    # Parent array index:
    i = 0

    # Child array indices:
    l = 0
    r = 0

    # Swap elements while there's a pair of numbers
    # being processed simultaneously.
    # Must process at least one number from each
    # side
    while ((l < leftSize) and (r < rightSize)):

        if (leftArray[l] < rightArray[r]):
            array[i] = leftArray[l]
            l += 1
        else:
            array[i] = rightArray[r]
            r += 1

        # increment parent array index:
        i += 1

    # One side remains with numbers:
    # Check left:
    while (l < leftSize):
        array[i] = leftArray[l]
        l += 1
        i += 1

    # Check right:
    while (r < rightSize):
        array[i] = rightArray[r]
        r += 1
        i += 1


def mergeSort(array):
    # Divide the input in two parts: left and right:
    arraySize = len(array)
    # Stop recursion when the maximum number of
    # divisions have been reached:
    if (arraySize == 1):
        return

    # Get the middle of the array:
    middle = arraySize // 2
    # Create left and right arrays:
    leftArray = [0] * middle
    rightArray = [0] * (arraySize - middle)

    # Populate both arrays:
    l = 0  # left index
    r = 0  # right index
    for i in range(arraySize):
        # Populate left:
        if (i < middle):
            leftArray[l] = array[i]
            l += 1
        # Populate right:
        else:
            rightArray[r] = array[i]
            r += 1

    # Recursive call to the same function
    # until right and lefth have only one
    # item each:
    mergeSort(leftArray)
    mergeSort(rightArray)
    print((leftArray, rightArray))
    # Swap-merge both numbers/arrays:
    merge(leftArray, rightArray, array)
    print(array)


# Test case:
array = [8, 2, 5, 3, 4, 7, 6, 1]

mergeSort(array)
print(array)
