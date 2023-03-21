# File        :   addTwoNumbers.py
# Version     :   1.0.0
# Description :   Solution to the (bullshit) addTwoNumbers problem
#                
# Date:       :   Mar 21, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# NOTE:
# No linked lists are used here, since I'm writing this solution in Python. Python does not
# handle explicit use of references and pointers, it defeats one of its core purposes - to write
# code easily and quickly.
# Linked lists implemented on Python are bullshit. Python lists are used instead, as the example 
# uses lists anyway...

def addTwoNumbers(l1, l2):

    # Get lists lengths:
    l1Length = len(l1)
    l2Length = len(l2)

    # Absolute difference between lists:
    absDiff = abs(l1Length - l2Length)
    # biggestList = l1Length

    # Check lists sizes, they must match:
    if (l1Length != l2Length):
        # Resize smallest list accordingly,
        # Pad the target list with zeros:
        if (l1Length > l2Length):
            l2 = l2 + [0] * absDiff
        else:
            l1 = l1 + [0] * absDiff
            # biggestList = l2Length

    # Carries list:
    carries = [0] * (len(l1) + 1)
    # Out list:
    outList = []

    for i in range(len(l1)):
        # Add numbers + carries:
        numberSum = l1[i] + l2[i] + carries[i]
        # Check magnitude:
        if (numberSum >= 10):
            # Just one column:
            numberSum = numberSum - 10
            # Carry over the 10s:
            carries[i + 1] = 1
        # Store number sum:
        outList.append(numberSum)

    # Add the last carry:
    lastCarry = carries[len(carries) - 1]
    if (lastCarry == 1):
        outList.append(1)

    # Done:
    return outList


# Test case entry:
l1 = [2,4,3]
l2 = [5,6,4]

# Get the result:
outRes = addTwoNumbers(l1, l2)
print(outRes)
