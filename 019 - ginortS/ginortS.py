# File        :   ginortS.py
# Version     :   1.0.0
# Description :   Solution to the ginortS problem
#                
# Date:       :   Feb 25, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Sample Input:
# s = "Sorting1234"

# Sample Output:
# "ginortS1324"

# Check if a number is even or odd:
def isEven(n):
    outValue = False
    if (n % 2) == 0:
        outValue = True
    return outValue

# Set input string:
s = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"

# Get string length:
stringLength = len(s)

# Set the sorting lists:
lower = []
upper = []
odd = []
even = []

# Loop through each character and "classify it"
# store it in the proper list:
for c in range(stringLength):
    # Get current char:
    currentChar = s[c]

    # Check if letter:
    if (currentChar.isalpha()):
        # Check if upper case:
        if (currentChar.isupper()):
            # Goes into the upper case list:
            targetList = upper
        else:
            # Goes into the lower case list:
            targetList = lower
    else:
        # Cast to integer:
        currentNumber = int(currentChar)
        # Check if even:
        if (isEven(currentNumber)):
            # Goes into the even list:
            targetList = even
        else:
            # Goes into the odd list:
            targetList = odd

    # Append into corresponding list:
    targetList.append(currentChar)

# Sort letters alphabetically:
lower.sort()
upper.sort()

# Sort numbers from smallest to largest:
odd.sort()
even.sort()

# Create final String:
outString = lower + upper + odd + even
outString = "".join(outString)

print(outString)