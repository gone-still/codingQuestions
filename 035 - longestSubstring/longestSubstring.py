# File        :   longestSubstring.py
# Version     :   1.0.0
# Description :   Solution to the longestSubstring problem
#                
# Date:       :   Mar 27, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string s, find the length of the longest substring without 
# repeating characters.

# Input: s = "pwwkew"
# Output: 3

# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence 
# and not a substring.

def longestSubstring(s):
    # Check for valid string:
    if (len(s) < 1):
        return 0

    # Repeat last character:
    s = s + s[-1]

    # Base variables:
    charDict = {} # Character dictionary

    stringBuff = ""
    stringLength = -1

    maxLength = -1
    maxSubString = ""
    currentString = ""

    lastIndex = 0
    startIndex = 0
    currentIndex = 0

    # Loop through the string, one character
    # at a time:
    for c in s:

        # Update char buffer:
        currentString = currentString + c

        # Look for character entry in dictionary:
        if c not in charDict:
            # Create a new entry:
            charDict[c] = currentIndex
        else:
            # Check that new entry is in range withing the current
            # substring's indices:
            lastIndex = charDict[c]

            if (lastIndex >= startIndex):
                # Debug info, show the new string built so far:
                currentString = s[lastIndex + 1:currentIndex + 1]
                # Get current max substring:
                stringBuff = s[startIndex:currentIndex]
                # Start index is now current index:
                startIndex = lastIndex + 1

                # Check if larget than previous stored
                # index:
                stringLength = len(stringBuff)

                if (stringLength > maxLength):
                    maxSubString = stringBuff
                    maxLength = stringLength

            # Store character with current index
            charDict[c] = currentIndex

        # Increase char counter:
        currentIndex += 1

    # Print both the substring and its
    # max length:
    print(maxSubString, maxLength)

    # Done
    return maxLength

# Test case:
s = "fvcktechintervi3ws"
l = longestSubstring(s)
print(l)
