# File        :   partitionString.py
# Version     :   1.0.0
# Description :   Solution to the partitionString problem
#                
# Date:       :   Apr 04, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string s, partition the string into one or more substrings such that the characters 
# in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 
# Example 1:
# Input: s = "abacaba"
# Output: 4

# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

def partitionString(s):
    # Extend last char:
    s = s + s[-1]

    stringBuffer = ""
    localDict = {}

    stringLength = len(s)
    stringIndex = 0

    totalSubstrings = 0

    substringsList = []
    processString = True

    while (processString):

        # Get current char:
        currentChar = s[stringIndex]
        # Build current string buffer, one char at the time:
        stringBuffer = stringBuffer + currentChar

        # Check if entry exists in char dir:
        if currentChar not in localDict:
            # Add one entry:
            localDict[currentChar] = 1
            stringIndex += 1
        else:
            # Drop last char:
            stringBuffer = stringBuffer[:-1]
            localDict.clear()

            # Count goes up:
            totalSubstrings += 1

            # Store substring:
            substringsList.append(stringBuffer)
            stringBuffer = ""

            # Check if all chars have been processed:
            if stringIndex == stringLength-1:
                processString = False

    # Print list of sub-strings:
    print(substringsList)
    return totalSubstrings


s = "hdklqkcssgxlvehva"
t = partitionString(s)
print(t)
