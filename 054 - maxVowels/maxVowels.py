# File        :   infiniteSet.py
# Version     :   1.0.0
# Description :   Solution to the maxVowels problem
             
# Date:       :   May 12, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string s and an integer k, return the maximum number of vowel letters 
# in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3

# Explanation: The substring "iii" contains 3 vowel letters.

def maxVowels(s, k):
    # Create voc of vowels:
    vowelsDict = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
    stringLength = len(s)
    # Store max vowel count here:
    maxCount = 0
    # Local vowel counter:
    vowelCount = 0

    # Loop through all the characters of the string:
    for i in range(stringLength):
        # Process the first characters before filling
        # up the window:
        if i < k:
            # Get current character:
            c = s[i]
            # Check if it is vowel:
            if c in vowelsDict:
                # Counter goes up +1
                vowelCount += 1

        # The window has been filled. Just check first
        # character that "exits" the window and the last
        # that enters it:
        else:
            # Get first char:
            first = s[i - k]
            if first in vowelsDict:
                vowelCount -= 1
            # Get last char:
            last = s[i]
            if last in vowelsDict:
                vowelCount += 1

        # Check if the count is maximum:
        if vowelCount > maxCount:
            maxCount = vowelCount

    # Done:
    return maxCount


s = "singasong"
k = 4
o = maxVowels(s, k)
print("Out:", o)
