# File        :   questionMarks.py
# Version     :   1.0.0
# Description :   Solution to the questionMarks problem

# Date:       :   Ma 20, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers 
# that add up to 10. If so, then your program should return the string true, otherwise it should return the string 
# false. If there aren't any two numbers that add up to 10 in the string, then your program should return false 
# as well. 

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 
# 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 


def QuestionsMarks(strParam):

    # Function variables:
    outString = "false"

    numSum = 0          # Stores the sum of two numbers
    gotNumber = False   # Flag that indicates the detection of a number
    charCount = 0       # Target character counter (?)
    pastNumber = 0      # Past detected number

    # Loop through the string
    for c in strParam:

        # Check if current char is numeric:
        if (c.isnumeric()):
            # Convert the char to int:
            c = int(c)

            # Got numebr flag:
            gotNumber = not(gotNumber)

            # End of target flag switch:
            if not(gotNumber):

                # Check number sum:
                numSum = pastNumber + c

                # Need the pair to addd up to 10:
                if (numSum == 10):
                    # Target character count needs
                    # to be 3:
                    if (charCount == 3):
                        outString = "true"
                    else:
                        outString = "false"
                        break

            # Clear char count every time a number
            # is detected and the previous count was
            # processed:
            charCount = 0

            # Current number is now past number:
            pastNumber = c
            gotNumber = True

        else:
            # Check if current char is "?"
            if (gotNumber):
                if (c == "?"):
                    charCount += 1
            else:
                # If current char is not numeric or "?"
                # and no previous number was detected,
                # clear the char count:
                charCount = 0
                gotNumber = False

    # Done, no regex:
    return outString


# Test case entry:
s = "acc?7??sss?3rr1??????5"
print(QuestionsMarks(s))

