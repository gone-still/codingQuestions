# File        :   groupAnagrams.py
# Version     :   1.0.0
# Description :   Solution to the groupAnagrams problem
#
# Date:       :   May 30, 2023
# Author      :   Ricardo Acevedo-Avila
# License     :   Creative Commons CC0

def groupAnagrams(strs):
    # Dictonary that stores string anagrams:
    anagramsDict = {}
    # Dictionary that stores strings by anagram group:
    groupDict = {}
    groupCounter = 0

    # Group strings:
    for s in strs:
        # Sort string:
        sortedString = sorted(s)
        # Join each character into a word (string):
        sortedString = "".join(sortedString)

        # Current string not in dict:
        if sortedString not in anagramsDict:
            # Group counter increases by 1:
            groupCounter += 1
            # Sorted string goes into anagram dict:
            anagramsDict[sortedString] = groupCounter
            # Original string goes into group dict:
            groupDict[groupCounter] = [s]

        # String is anagram:
        else:
            # Get its group:
            stringGroup = anagramsDict[sortedString]
            # Store in group dict:
            groupDict[stringGroup].append(s)

    # Get dict keys and store them into the output list:
    result = []
    for key in groupDict:
        currentList = groupDict[key]
        result.append(currentList)

    return result


# Test case:
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
out = groupAnagrams(a)
print("Out:", out)
