# File        :   findIntersection.py
# Version     :   1.0.0
# Description :   Solution to the findIntersection problem
#
# Date:       :   Mar 18, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will 
# contain 2 elements: the first element will represent a list of comma-separated numbers sorted in 
# ascending order, the second element will represent a second list of comma-separated numbers 
# (also sorted). 

# Your goal is to return a comma-separated string containing the numbers that occur in elements of 
# strArr in sorted order. If there is no intersection, return the string false.

def FindIntersection(strArr):
    # Create the counter dictionary:
    countsDict = {}

    # Get first and second array of strings:
    firstArray = strArr[0]
    secondArray = strArr[1]

    # Strip white spaces and concatenate
    # an "," at the end of each string, which
    # acts as a "eol":
    firstArray = firstArray.replace(" ", "")
    firstArray = firstArray + ","
    secondArray = secondArray.replace(" ", "")
    secondArray = secondArray + ","

    # Loop through the first string. Create a char buffer
    # if current char is not ",". If current char is ","
    # dump the char buffer into disctionary with a count of "1":
    charBuff = ""
    for c in firstArray:
    	# No comma, keep bulding the buffer:
        if (c != ","):
            charBuff = charBuff + c
        # Comma, dump the buffer into dict:
        else:
            # Check dict entry:
            if charBuff not in countsDict:
            	# Mark it:
                countsDict[charBuff] = 1
            charBuff = ""

    # Loop trhough the second string, get a char buffer of
    # comma-separated substrings and check for dictionary count:
    charBuff = ""
    outString = ""
    for c in secondArray:
    	# No comma, keep bulding the buffer:
        if (c != ","):
            charBuff = charBuff + c
        # Comma, dump the buffer into dict:
        else:
            # Check dict entry:
            if charBuff in countsDict:
            	# Construct the out string:
                outString = outString + charBuff + ","
            charBuff = ""

    # Intersections found, strip the last comma:    
    if (outString != ""):
        outString = outString[:-1]
    # No intersections found, the out string is empty:  
    else:
        outString = "false"
    # Done:
    return outString

# Keep this function call here
arr = ["5, 3, 7, 10, 17, 18", "1, 4, 9, 11"]
print(FindIntersection(arr))
