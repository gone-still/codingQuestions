# File        :   missingInteger.py
# Version     :   1.0.0
# Description :   Solution to the missingInteger problem
#                
# Date:       :   Apr 20, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Write a function:
# class Solution { public int solution(int[] A); }
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) 
# that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

def missingInteger(a):
    # Create dictionary from list:
    numberDict = dict.fromkeys(a, 1)
    # Get list length:
    listLength = len(a)
    # Set default out value.
    # This value is given if all the integers are
    # found in the list. In that case, the function
    # should return the next greater integer:
    outInteger = listLength + 1

    for i in range(listLength):
        # Check if target in dict:
        target = i + 1
        if target not in numberDict:
            # If entry not found, this is
            # the missing integer:
            outInteger = target
            break
    # Done:
    return outInteger


# Test case entry:
a = [1, 3, 999999, 999998, 1000000]
outInteger = missingInteger(a)
print("out:", outInteger)
