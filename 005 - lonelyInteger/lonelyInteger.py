# File        :   lonelyInteger.py
# Version     :   1.0.0
# Description :   Solution to the lonelyInteger problem
#                
# Date:       :   Feb 03, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of integers, where all elements but one occur twice, 
# find the unique element.

# Example: a = [1, 2, 3, 4, 3, 2, 1]

# The unique element is: 4

def lonelyinteger(a):
    # Size of the list:
    listSize = len(a)

    # Flag that keeps track of
    # the lonely integer search
    foundNumber = False

    # The lonely integer is stored here:
    outNumber = -1

    # Loop trhough the numbers list:
    for i in range(listSize):
        # Get current number:
        currentNumber = a[i]

        # Check if the current number has already
        # been processed:
        if currentNumber != -1:
            
            # Set found flag:
            foundNumber = True

            # Loop through the rest of the list:
            for j in range(i + 1, listSize):
                # Get next immediate number:
                targetNumber = a[j]

                # Check if it is a duplicate:
                if currentNumber == targetNumber:
                    # Set found flag to false:
                    foundNumber = False
                    # Mark processed numbers:
                    a[i] = -1
                    a[j] = -1
                    break

            # If the end of the list has been reached,
            # check found flag:
            if foundNumber:
                # Lonely integer has been found:
                outNumber = currentNumber
                break

    # Done:
    return outNumber


if __name__ == '__main__':

    a = [1, 2, 3, 4, 3, 2, 1]
    result = lonelyinteger(a)

    print(result)
