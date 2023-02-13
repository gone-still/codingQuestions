# File        :   salesByMatch.py
# Version     :   1.0.0
# Description :   Solution to the salesByMatch problem
#                
# Date:       :   Feb 12, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# There is a large pile of socks that must be paired by color. Given an array of 
# integers representing the color of each sock, determine how many pairs of socks 
# with matching colors there are.

# Example:

# arr = [1, 2, 1, 2, 1, 3, 2]
# n = 7

# There is one pair of color 1 and one of color 2. There are three odd socks left, 
# one of each color. The number of pairs is 2.


import math


def sockMerchant(n, arr):

    # Prepare the dictionary of items,
    # valures are stored as a tuple of 3 elements:
    # for everyr Color -> (colorCount, pairs, singles)
    socksDic = {}

    # Loop through the item list:
    for i in range(n):

        # Get current item
        currentItem = arr[i]

        # Check if entry exists:
        if currentItem in socksDic:

            # Increase item count:
            currentCount = socksDic[currentItem][0]
            currentCount += 1

            # Compute current pairs:
            currentPair = math.floor(currentCount / 2)

            # Compute current singles:
            currentSingles = math.ceil(currentCount - 2 * currentPair)

            # Into the dictionary:
            socksDic[currentItem] = (currentCount, currentPair, currentSingles)

        else:

            # No previous entry, set first entry:
            socksDic[currentItem] = (1, 0, 1)

    # Total pairs found:
    totalPairs = 0

    # Loop through the dictionary and print the info:
    for i, _ in socksDic.items():
        # GEt dictionary data:
        currentItem = socksDic[i]
        itemCount = currentItem[0]
        itemPairs = currentItem[1]
        itemSingles = currentItem[2]

        # Accumulate pairs obtained so far:
        totalPairs = itemPairs + totalPairs

        # Print the info:
        print(
            "Color: " + str(i) + " Total: " + str(itemCount) + " Pairs: "
            + str(itemPairs) + " Singles: " + str(itemSingles)
        )

    # Done:
    return totalPairs


# Test case entry:

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(arr)

totalPairs = sockMerchant(n, arr)

print(totalPairs)
