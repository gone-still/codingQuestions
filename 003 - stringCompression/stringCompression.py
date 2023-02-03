# File        :   stringCompression.py
# Version     :   1.0.0
# Description :   Solution to the string compression problem
#                
# Date:       :   Feb 03, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . 
# To read more about this function, Check this out.

# You are given a string "S". Suppose a character "c" occurs consecutively "X"  times in the string. 
# Replace these consecutive occurrences of the character "c" with "(X,c)" in the string.

# Sample Input: "1222311"
# Sample Output: "(1, 1) (3, 2) (1, 3) (2, 1)"

# Also, note the single space within each compression and between the compressions.

# Receive input:
inputString = input()

# Get string length:
stringLength = len(inputString)

# Prepare char buffer, first char same as string:
pastChar = inputString[0]

# Occurence counter:
charCounter = 0

# Prepare out string:
compressedString = ""

# Process the string:
for i in range(stringLength):
    
    # Get chars:
    currentChar = inputString[i]

    # If different from buffer, store in out string:
    if (pastChar != currentChar):
        compressedString = compressedString + "("+str(charCounter)+", "+pastChar+")" + " "
        # Reset occurence counter:
        charCounter = 0

    # Ready for next iteration
    pastChar = currentChar
    charCounter += 1


# String end data dump:
compressedString = compressedString + "("+str(charCounter)+", "+pastChar+")"

# Done
print(compressedString)