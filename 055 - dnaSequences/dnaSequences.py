# File        :   dnaSequences.py
# Version     :   1.0.0
# Description :   Solution to the dnaSequences problem
#                
# Date:       :   May 24, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
# that occur more than once in a DNA molecule. You may return the answer in any order.

 
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]


def findRepeatedDnaSequences(s, k):
    # Get string length:
    stringLength = len(s)

    # If string is smaller or equal
    # then input, return empty list:
    if stringLength <= k:
        return []

    # Occurrences counter:
    counter = {}
    # Get substring:
    substring = s[0:k]
    # Into counter:
    counter[substring] = 1
    stringEnd = stringLength - k
    # out list:
    result = []

    # Slice strings and store them in
    # counter dictionary:
    for i in range(1, stringEnd + 1):
        # Slice:
        currentSubstring = s[i:i + k]
        # Count:
        if currentSubstring not in counter:
            # First count:
            counter[currentSubstring] = 1
        else:
            # More than once:
            counter[currentSubstring] += 1
            # Check if it has been stored before:
            if currentSubstring not in result:
                # Into result list
                result.append(currentSubstring)
    # Done:
    return result


# Test case:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
k = 10
out = findRepeatedDnaSequences(s, k)
print("Out:", out)
