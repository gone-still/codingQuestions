# File        :   addBinary.py
# Version     :   1.0.0
# Description :   Solution to the addBinary problem
#
# Date:       :   Apr 01, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
def addBinary(a, b):
    # Strings to list:
    a = list(a)
    b = list(b)

    # Get the array size:
    aLength = len(a)
    bLength = len(b)

    # Differences between lists:
    absDiff = abs(aLength - bLength)

    # Fill smallest list and carry list
    # with the necessary zeros:
    if aLength > bLength:
        b = [0] * absDiff + b
        c = [0] * (aLength + 1)
        bLength = len(b)
    else:
        a = [0] * absDiff + a
        c = [0] * (bLength + 1)
        aLength = len(a)

    # Sum dictionary. Implements the
    # truth table of the addition of three bits-> carry + a + b:
    stringDict = {"000": ["0", "0"], "001": ["1", "0"], "010": ["1", "0"], "011": ["0", "1"],
                  "100": ["1", "0"], "101": ["0", "1"], "110": ["0", "1"], "111": ["1", "1"]}
   
    stringResult = ""
    sliceIndex = -1
    allZeros = True

    for i in range(aLength - 1, -1, -1):
        # Get individual "bits"
        cBit = str(c[i + 1])
        aBit = str(a[i])
        bBit = str(b[i])

        # Create "word" and look it up in
        # the dictionary
        currentKey = cBit + aBit + bBit
        currentValue = stringDict[currentKey]

        # Concatenate result bit:
        stringResult = currentValue[0] + stringResult

        # Carry over sum overflow:
        c[i] = currentValue[1]

        # Store the index of a possible
        # leading zero:
        if currentValue[0] == "1":
        	# Reset the index if current bit
        	# is "1":
            sliceIndex = -1
        elif sliceIndex == -1:
        	# Update index only if past bit
        	# was "1" and now is "0":
            sliceIndex = i

        # All zeros condition:
        if currentKey != "000":
            allZeros = False

    # Check carry out:
    if c[0] == "1":
        # if carry set, concatenate an extra "1" at the MSB:
        stringResult = "1" + stringResult
    # Check if leading zeros should be removed:
    elif sliceIndex != -1:
        # Slice out them zeros:
        stringResult = stringResult[sliceIndex + 1:aLength + 1]

    # Check all zeros:
    if allZeros:
    	# Output is just "0":
        stringResult = "0"

    return stringResult


# Test case entry:

# Set the input lists:
a = "11001110100100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b = "10011010010100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"

# Get the binary string:
sumString = addBinary(a, b)
print(sumString)
