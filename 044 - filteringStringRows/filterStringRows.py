# File        :   filterStringRows.py
# Version     :   1.0.0
# Description :   Solution to the filterStringRows problem
#                
# Date:       :   Apr 10, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Write a solution that that removes a row of a table if one of the cells contain a NULL, such as 
# row with the name Jenny. The table is given in CSV format.Every two consecutive cells in each row 
# are separated by a single comma ',' symbol. Every two consecutive rows are separated by a new-line 
# '\n' symbol

# Example:
# Given S = "id,name,age,score\n1,Jenny,NULL,14\n17,Daryll,31,11", your function should return 
# "id,name,age,score\n17,Betty,28,11"

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


# Test case entry:
inputString = "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11"
# Process the input:
filteredString = filterRows(inputString)
# Print result:
print(filteredString)
