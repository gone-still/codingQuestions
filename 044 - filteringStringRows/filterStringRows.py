# File        :   filterStringRows.py
# Version     :   1.0.1
# Description :   Solution to the filterStringRows problem
#                
# Date:       :   Jan 30, 2024
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Write a solution that that removes a row of a table if one of the cells contain a NULL, such as 
# row with the name Jenny. The table is given in CSV format.Every two consecutive cells in each row 
# are separated by a single comma ',' symbol. Every two consecutive rows are separated by a new-line 
# '\n' symbol

# Example:
# Given S = "id,name,age,score\n1,Jenny,NULL,14\n17,Daryll,31,11", your function should return 
# "id,name,age,score\n17,Betty,28,11"

# Original Solution:
def filterRows(inputString):
    #  The filtered strings are stored here:
    filtered = []

    # Separate \n terminating lines:
    for line in inputString.splitlines():
        # Get current line
        currentLine = line.split(",")
        # Search for "NULL"
        if "NULL" not in currentLine:
            # If not NULL, append:
            filtered.append(currentLine)

    # Out String:
    outString = ""
    totalRows = len(filtered)
    for i, line in enumerate(filtered):
        # Format current line:
        currentLine = ",".join(line)
        # Do not append "\n" to the last line: 
        if (i < totalRows-1):
            currentLine = currentLine + "\n"
        # Append to out string:
        outString = outString + currentLine

    return outString


# New Solution:
def filterRowsNew(inputString: str) -> str:
    """Receives a string representing lines with "\n" and 
     filters lines that have "NULL" in any cell"""

    # Set outstring:
    outString = ""

    # Break strings ending with "\n" into lines:
    lines = inputString.split("\n")

    # For each line...
    for line in lines:
        # Split the string into individual words:
        cells = line.split(",")

        # Search for keyword in list of words:
        if "NULL" not in cells:
            # If not found, append original string to
            # outstring. Append end of line char:
            outString += line + "\n"

    # Remove end of line char last appended:
    outString = outString[:-1]

    return outString


# Test case entry:
inputString = "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11\n17,Daryll,31,11\nNULL,Eric,69,420"
# Process the input:
filteredString = filterRows(inputString)
# Print result:
print(filteredString)

# Test new solution:
# Process the input:
filteredString = filterRowsNew(inputString)
# Print result:
print(filteredString)