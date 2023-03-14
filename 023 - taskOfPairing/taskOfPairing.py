# File        :   taskOfPairing.py
# Version     :   1.0.0
# Description :   Solution to the taskOfPairing problem
#                
# Date:       :   Mar 13, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# A gym manager is trying to pair dumbbells. You are given a frequency array. This array 
# means the index equals (dumbbell_weight - 1) and the value equals number_of_dumbbells. 
# The manager is okay with mixing weights, so long as the weight difference is no more than 1 
# (e.g. a 14lb dumbbell can be matched with a 15lb dumbbell and a 15lb dumbbell with a 16lb dumbbell). 
# How many of these pairs can you make?

# Example:
# freq = [3,2,3,2]
# 1lb: 3
# 2lb: 2
# 3lb: 3
# 4lb: 2

# These can be paired as [[1,1], [1,2], [2,3], [3,3], [4,4]], which means we have 5 pairs.

# Even or odd:
def isEven(n):
    outValue = False
    if (n % 2 == 0):
        outValue = True

    return outValue


def getPairs(a):
    # Counts pairs:
    pairCounter = 0
    # Counts singles:
    singleCounter = 0
    for i in range(len(a)):
        # Get current item:
        currentItem = a[i]
        # Get how many pairs of this item:
        currentPairs = math.floor(0.5 * currentItem)
        # Accumulate all pairs so far:
        pairCounter = pairCounter + currentPairs

        # Check if current item is 0,
        # if so, you can't "propagate"
        # the single element and make a pair:
        if (currentItem == 0):
            singleCounter = 0
        else:
            # Element is non-zero, is it even?
            evenValue = isEven(currentItem)
            # If not, a single can be produced:
            if not (evenValue):
                # Count an extra single:
                singleCounter += 1
                # Two singles make a pair:
                if (singleCounter == 2):
                    pairCounter = pairCounter + 1
                    # Reset the single counter:
                    singleCounter = 0
    # Ready:
    return pairCounter

# Test case:
a = [1, 1, 1, 0, 2, 3, 1]

totalPairs = getPairs(a)

print(totalPairs)
