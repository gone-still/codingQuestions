# File        :   wordPattern.py
# Version     :   1.0.0
# Description :   Solution to the wordPattern problem
#                
# Date:       :   Apr 20, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 
def wordPattern(pattern, s):
    # Split string into list of words:
    wordList = s.split(" ")
    # Get lists lengths:
    totalWords = len(wordList)
    patternLength = len(pattern)

    # Both number of elements must match:
    if patternLength != totalWords:
        return False
    # First dictionary associates pattern character
    # with word. Second dictionary associates word
    # with character/symbol. 
    # No repetitions must be present:
    wordDict = {}
    wordSymbol = {}

    outValue = True

    # Loop through each character making up
    # the pattern:
    for i, c in enumerate(pattern):
        # Get word from list:
        listWord = wordList[i]
        # Loo if the character has a word associated
        # to it:
        if c not in wordDict:
            # If not, create association:
            wordDict[c] = listWord
            # Associate character with word too,
            # must be a unique association:
            if listWord not in wordSymbol:
                wordSymbol[listWord] = c
            else:
            # Theres a character associated with this
            # same word, and it shouldn't:
                outValue = False
                break
        else:
            # Check if the character is associated to the
            # expected word:
            storedWord = wordDict[c]
            if storedWord != listWord:
                outValue = False
                break
    # Done:
    return outValue


# Test case entry:
pattern = "abbc"
s = "dog dog dog cat"
outResult = wordPattern(pattern, s)
print("out:", outResult)
