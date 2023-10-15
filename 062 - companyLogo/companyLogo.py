# File        :   companyLogo.py
# Version     :   1.0.0
# Description :   Solution to the companyLogo problem
#                
# Date:       :   Oct 14, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# A newly opened multinational brand has decided to base their company logo on the three most common characters 
# in the company name. They are now trying out various combinations of company names and logos based on this 
# condition. Given a string , which is the company name in lowercase letters, your task is to find the top three 
# most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Input Format
# A single line of input containing the string .

# Constraints
# S has at least  distinct characters
# Output Format

# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0
# aabbbccde

# Sample Output 0

# b 3
# a 2
# c 2

# Explanation:
# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line and c in the third line because 
# a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.

def companyLogo(s):
    # Set word counter:
    wordCounter = {}
    for c in s:
        # Already in dict, increment count +1
        if c in wordCounter:
            wordCounter[c] += 1
        # Not in dict, first count:
        else:
            wordCounter[c] = 1

    # Here goes my nasty dict stop entry:
    wordCounter["zztop"] = -69
    # Sort by occurrence:
    sortedDict = dict(sorted(wordCounter.items(), key=lambda item: item[1], reverse=True))

    # Some variables
    tempList = []  # Holds repeated chars by occurrence
    outList = []  # Holds out tuple of (key/char, count)
    pastCount = 0  # For last vs current count comparison
    getLast = True  # Get last stored char (to be ordered along same-occurrence chars)

    # Loop through the ordered dict:
    for i, key in enumerate(sortedDict):

        # Get current char count:
        currentCount = sortedDict[key]

        # Check against past:
        if pastCount != currentCount:

            # Check out the temp list that holds all chars with same occurrence.
            # If the list is not empty, there are elements to be alpha-sorted:

            if len(tempList) > 0:
                # Sort list:
                tempList.sort()
                # Concatenate to out list:
                outList += tempList
                # Clear list:
                tempList = []

            # Need to  get next same-occurrence char from out list:
            getLast = True
            # Current char (where the occurrence was different from last)
            # goes into out list:
            outList.append((key, currentCount))

            # If there are 3 elements in out list, we are done
            # and hackerrank can go fuck itself:
            if len(outList) >= 3:
                # Just need the 3 top elements:
                outList = outList[0:3]
                break

        else:

            # Got same occurrence than last char, gotta fetch the
            # last stored element:
            if getLast:
                # Get last tuple:
                lastTuple = outList[-1]
                # Into temp list:
                tempList.append(lastTuple)
                # Remove last from out list tuple:
                outList.pop()
                getLast = False

            # Append current key and count:
            tempList.append((key, currentCount))

        # Present is now past:
        pastCount = currentCount

    # Final print:
    print("Final Result: ")
    for currentTuple in outList:
        print(currentTuple[0], currentTuple[1])


# Run the test case:
if __name__ == '__main__':
    s = "fuckHackerRank"
    companyLogo(s.lower())
