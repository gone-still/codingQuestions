# File        :   stringMatching.py
# Version     :   1.0.0
# Description :   Solution to the stringMatching problem
              
# Date:       :   Mar 23, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given two strings needle and haystack, return the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.

# Example:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Solution:
# Implement a cross-correlation operation, albeit, with some modifications. Get a sub-string 
# window of the haystack characters with the needle's string size. 
# Slide it to the left, across the haystack, one character at the time. At each iteration 
# compare the window with the needle. Stop when both strings match.

def stringMatching(haystack, needle):
    # Base variables:
    outIndex = -1
    haystackLength = len(haystack)
    needleLength = len(needle)

    # Check for valid string size:
    if (needleLength < 1) or (haystackLength < 1):
        return outIndex

    # Loop through the haystack, implementing the
    # modified "cross-correlation":
    for i in range(haystackLength):
        # Get "window" length:
        windowLength = needleLength
        # Get sliding window:
        window = haystack[i:i + windowLength]
        # Check for match:
        if (window == needle):
            outIndex = i
            break

    return outIndex


# Test case:
haystack = "bigbaddog"
needle = "dog"

outIndex = stringMatching(haystack, needle)
print(outIndex)
