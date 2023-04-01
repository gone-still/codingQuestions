# File        :   phoneCombinations.py
# Version     :   1.0.0
# Description :   Solution to the phoneCombinations problem, solved by using breadth search.
#                
# Date:       :   Mar 31, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the 
# number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below:

# { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

# Note that 0/1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

def breadthSearch(searchDepth, currentLevel, stringBuff, charDict, digits, combinations):
    # Reach end of the branch:
    if (currentLevel == searchDepth):

        # Store string buffer in list:
        combinations.append(stringBuff)
        return

    # Keep traversing the tree's nodes:
    else:
        # Get current set of char for this level
        # That is, the "breadth" of the code
        currentChar = digits[currentLevel]
        currentBreadth = charDict[currentChar]

        # For each char/node, traverse each brach:
        for c in currentBreadth:
            # Traverse next node:
            breadthSearch(searchDepth, currentLevel + 1, stringBuff + c, charDict, digits, combinations)


def letterCombinations(digits):
    # If digits empty, return empty
    # list:
    if digits == "":
        return []

    # Numbers -> letters mapping:
    charDict = {"0": "", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                "9": "wxyz"}

    # Out list with combinations. To be modified by reference:
    combinations = []

    # String buffer. Stores the concatenation of each character for
    # each tree node:
    stringBuff = ""

    # Total depth of the tree:
    searchDepth = len(digits)

    # Call to the recursive function to create and traverse tree's branches:
    breadthSearch(searchDepth, 0, stringBuff, charDict, digits, combinations)

    return combinations


# Test case entry:
digits = "234"
combinations = letterCombinations(digits)
print(combinations)
