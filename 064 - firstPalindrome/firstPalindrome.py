# File        :   firstPalindrome.py
# Version     :   1.0.0
# Description :   Solution to the Longest Valid Parentheses problem
#
# Date:       :   Feb 15, 2024
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of strings words, return the first palindromic string in the array.
# If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

import array


def firstPalindromeQuick(words: list) -> str:
    """
    :type words: The list of words
    :rtype: First palindrome string in the list
    """
    outString = ""
    for currentWord in words:
        # Reverse word:
        reversedWord = currentWord[::-1]
        # Compare strings:
        if currentWord != reversedWord:
            # On to the next one:
            continue
        else:
            # Got palindrome:
            outString = currentWord
            break

    # Done
    return outString


def firstPalindrome(words: list) -> str:
    """
    :type words: The list of words
    :rtype: First palindrome string in the list
    """
    outString = ""
    searchPalindrome = True
    k = 0
    totalWords = len(words)

    if totalWords > 0:
        while searchPalindrome:
            currentWord = array.array("u", words[k])
            wordLength = len(currentWord)
            for i, firstChar in enumerate(currentWord):
                # Compute index of last char:
                j = (wordLength - 1) - i

                # Get last char:
                lastChar = currentWord[j]

                # Check both chars, must be the same, if not
                # this is not a palindrome
                if firstChar != lastChar:
                    # on to the next word...
                    if k < totalWords - 1:
                        # More words to process:
                        k += 1
                    elif k == totalWords - 1:
                        # End of the list:
                        searchPalindrome = False
                    break

                # Reached the middle of the string:
                if i >= j:
                    # Found my palindrome:
                    outString = currentWord.tounicode()
                    searchPalindrome = False
                    break

    # Done:
    return outString


words = ["notapalindrome", "lol", "shit", "uwu"]
out = firstPalindromeQuick(words)
print("Max outString:", out)
