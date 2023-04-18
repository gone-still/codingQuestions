# File        :   mergeAlternately.py
# Version     :   1.0.0
# Description :   Solution to the mergeAlternately problem
               
# Date:       :   Apr 17, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end 
# of the merged string.

# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.

def mergeAlternately(word1, word2):
    # Get lists lengths:
    word1Length = len(word1)
    word2Length = len(word2)

    # Initialize lists indices:
    i = 0
    j = 0

    # Out string and stop flag:
    outString = ""
    appendCharacters = True

    # Append characters:
    while appendCharacters:

        # Process word 1:
        if i < word1Length:
            char1 = word1[i]
            outString = outString + char1
            i += 1

        # Process word 2:
        if j < word2Length:
            char2 = word2[j]
            outString = outString + char2
            j += 1

        # If all characters proceesed, end loop:
        if (i == word1Length) and (j == word2Length):
            appendCharacters = False

    # Done:
    return outString


# Test case entry:
word1 = "abcd"
word2 = "pq"
outString = mergeAlternately(word1, word2)
print("out:", outString)
