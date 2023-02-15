# File        :   palindromeIndex.py
# Version     :   1.0.0
# Description :   Solution to the palindromeIndex problem
#                
# Date:       :   Feb 14, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0


# Given a string of lowercase letters in the range ascii[a-z], determine the index of 
# a character that can be removed to make the string a palindrome. 

# There may be more than one solution, but any will do. 
# If the word is already a palindrome or there is no solution, return -1. 
# Otherwise, return the index of a character to remove.

# Example:

# s = "bcbc"

# Either remove 'b' at index 0 or 'c' at index 3.


# Reverse String Aux function:
def reverseString(inputString):
    return inputString[::-1]

# Main function:
def palindromeIndex(inputString):
    # Reverse input string:
    reversedString = reverseString(inputString)
    # Candidate indices are stored here:
    indices = []
    # Default value, assume that s is
    # already a palindrome:
    outIndex = -1

    # Loop through the input string:
    for c in range(len(s)):
        # Get each character from both original
        # and reversed strings:
        start = inputString[c]
        end = reversedString[c]

        # Check if the characters are the same:
        if start != end:
            # If not, this is a possible index to
            # delete:
            indices.append(c)

    # For all candidate indices, check which makes
    # the input string a palindrome:
    for i in range(len(indices)):
        # Get current index:
        currentIndex = indices[i]
        # Remove the character at that index:
        newString = s[0: currentIndex:] + s[currentIndex + 1::]
        # Get its reverse:
        newReverse = reverseString(newString)
        # If both strings are the same, we have a palindrome
        # and the index was good:
        if (newString == newReverse):
            # This is the character that needs
            # to be removed:
            outIndex = currentIndex
            # Exit loop:
            break

    # Done:
    return outIndex

# Test Case entry:
s = "bccbz"
characterIndex = palindromeIndex(s)
print(characterIndex)