# File        :   validParentheses.py
# Version     :   1.0.0
# Description :   Solution to the validParentheses problem
#                
# Date:       :   Mar 29, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string s containing just the characters '(', ')', '{', '}', '[' 
# and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()[]{}"
# Output: true

# Example 2:
# Input: s = "(]"
# Output: false

def isValid(s):
    outValue = True

    closeDict = {")": "(", "}": "{", "]": "["}
    charStack = []
    stackSize = 0

    for c in s:
        # Store char into the stack:
        charStack.append(c)
        stackSize += 1

        if c in closeDict:
            # Get closing pair for this char:
            openingChar = closeDict[c]
            currentChar = charStack[stackSize - 2]

            # Opening and current char must match:
            if (openingChar == currentChar):
                # Pop entries from stack:
                del charStack[stackSize - 2:stackSize]
                stackSize -= 2
            else:
                # Mismatching characters:
                outValue = False
                return outValue

    # Must end with an empty stack:
    if (stackSize != 0):
        outValue = False

    # Done:
    return outValue


# Set the input array:
inputArray = "([]{()[]}){}[[]]()"

# Check it symbols are balanced:
balanced = isValid(inputArray)
print(balanced)
