# File        :   largestPalindrome.py
# Version     :   0.9.0
# Description :   Solution to the largestPalindrome problem
#                
# Date:       :   Apr 23, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Note: One of the hardest yet. My solution is incomplete and 
# currently passes 98% (138/141) of the test cases. I've attached
# a case that is wrong. I'll get back to this problem sone day...

# Looks for a substring in a string,
# Returns if found along the matching index
# in the haystack:
def findSubstring(needle, haystack):
    needleLength = len(needle)
    haystackLength = len(haystack)
    for i in range((haystackLength - needleLength) + 1):
        window = haystack[i:needleLength + i]
        if window == needle:
            return (True, i)
    return (False, -1)


# Looks for largest possible palindrome in
# a string:
def longestPalindrome(s):
    stringLength = len(s)
    reversedString = s[::-1]

    stringBuffer = ""
    startIndex = 0
    endIndex = startIndex + 1

    checkFlags = [False, False]  # isSubstring, isPalindrome
    missedString = (-1, "")
    lastChar = ""
    currentChar = ""

    for i in range(stringLength):
        # Get substring
        substring = s[startIndex:endIndex]
        # Check if substring is in reverse string:
        isSubstring, reverseIndex = findSubstring(substring, reversedString)
        isPalindrome = False

        if isSubstring:
            # If substring found, check if palindrome...
            substringLength = len(substring)
            # Slice the original input string using the reversed indices:
            sliceStart = (stringLength - reverseIndex) - substringLength
            sliceEnd = stringLength - reverseIndex
            # Here's the original reversed substring:
            reversedSubsString = s[sliceStart:sliceEnd]

            # If the substring is a palindrome, it must match
            # on both the original and reversed formats:
            isPalindrome = (substring == reversedSubsString)
            if isPalindrome:
                # It matches, but is it the LARGEST substring so far?
                stringBufferLength = len(stringBuffer)
                if substringLength > stringBufferLength:
                    # It is, store in buffer:
                    stringBuffer = substring
                # Expand the substring window by one character...
                # Either because the current substring found wasn't the
                # largest or because it was the larges. Next substring
                # must be larger by one character:
                endIndex = endIndex + 1
            # Else, the substring wasn't a palindrome...
            else:
                endIndex = endIndex + 1
        else:
            # The substring wasn't found in the reversed string,
            # Move string window one character to the left:
            startIndex = startIndex + 1
            endIndex = endIndex + 1

            currentChar = substring[-1]
            wasValid = checkFlags[0]

            if wasValid:
                # Save possible missed string, but only if it
                # is larger than the substring in the buffer:
                substringLength = len(substring)
                stringBufferLength = len(stringBuffer)
                if substringLength > stringBufferLength:
                    # Goes into the list of possible missed substrings:
                    missedString = (substringLength, substring)
                # Clear state:
                checkFlags[0] = False
            else:
                # Check if I got two identical chars in the latest
                # run. This could be a potential palindrome:
                sameChar = (lastChar == currentChar)
                if sameChar:
                    print("Got same chars in string: ", substring)
                    # Gat all lengths...
                    substringLength = len(substring)
                    stringBufferLength = len(stringBuffer)
                    currentMissedLength = missedString[0]
                    # Only store candidate if it is at larger than the
                    # buffer and at least the same length of the already
                    # stored candidate:
                    if substringLength > stringBufferLength:
                        if substringLength >= currentMissedLength:
                            print("Replacin: ", missedString[1], "<-", substring)
                            missedString = (substringLength, substring)

        # Save state flags:
        if isSubstring and isPalindrome:
            checkFlags[0] = True
        # Store the last char:
        lastChar = substring[-1]

    # Check possible missed strings:
    missedStringLength = missedString[0]
    if missedStringLength != -1:
        # Get buffer length:
        bufferLength = len(stringBuffer)
        # Only interested on candidates larger than buffer:
        if missedStringLength > bufferLength:
            # Get candidate string:
            candidateString = missedString[1]
            print("Buffer: ", stringBuffer)
            print("Candidate: ", candidateString)
            # Set initial window size:
            windowStartSize = bufferLength + 1
            # Scale window from initial size to the candidates string's
            # length:
            for w in range(windowStartSize, missedStringLength, 1):
                # Set window size:
                windowSize = w
                # Scan the candidate string in search for palindromes
                # larger than the buffer's contents:
                for i in range((missedStringLength - windowSize) + 1):
                    currentWindow = candidateString[i:windowSize + i]
                    reversedWindow = currentWindow[::-1]
                    # Check if original substring and reversed are palindrome
                    if currentWindow == reversedWindow:
                        # They are, update buffer and gtfo:
                        stringBuffer = currentWindow
                        break
                else:
                    continue
                break

    return stringBuffer


# Test case entry:
string = "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftv" # out should be zqz
# string = "aacabkdacacaa"

outString = longestPalindrome(string)
print("out:", outString)
