# File        :   stringCompression2.py
# Version     :   1.0.0
# Description :   Solution to the stringCompression2 problem
#
# Date:       :   May 29, 2023
# Author      :   Ricardo Acevedo-Avila
# License     :   Creative Commons CC0

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the 
# input character array chars. Note that group lengths that are 10 or longer will be split into 
# multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.


# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


def compress(chars):
    # Append last different char:
    chars.append("-")
    # On first iteration, use first char
    # as past char:
    pastChar = chars[0]
    # Repetition counter:
    charCounter = 0
    # "Compressed" string is stored here as
    # a list of chars:
    compressed = []
    # Loop through all the chars, process one by one:
    for c in chars:
        # Compare current char vs past char:
        if c == pastChar:
            # They are the same, increment char counter:
            charCounter += 1
        else:
            # Got a different char, store the past char
            # into result array:
            compressed.append(pastChar)
            # Process count. If the count is greater than
            # 1, it must be appended to the result list:
            if charCounter > 1:
                # Int to String:
                charString = str(charCounter)
                # If counter length (as string) > 1 char,
                # split the counter into its individual
                # digits (very strange requirement):
                if len(charString) > 1:
                    # Split counter digits:
                    counterBuffer = list(charString)
                    # Append each digit to result
                    # list:
                    for b in counterBuffer:
                        compressed.append(b)
                else:
                    # Just append the counter as-is:
                    compressed.append(charString)
            # Count the processed char:
            charCounter = 1
        # Present is now past:
        pastChar = c

    # Get result length:
    result = len(compressed)
    # Pop last element (the extra character appended at the
    # very first step of the algorithm):
    chars.pop()
    # n first chars are replaced by "compressed" list of chars:
    chars[0:result - 1] = compressed

    return result


# Test case:
a = ["a", "a", "b", "b", "c", "c", "c"]
out = compress(a)
print("Out:", out)
