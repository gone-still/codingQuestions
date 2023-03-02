# File        :   gridChallenge.py
# Version     :   1.0.0
# Description :   Solution to the gridChallenge problem
#                
# Date:       :   Mar 01, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
# Determine if the columns are also in ascending alphabetical order, top to bottom. 
# Return YES if they are or NO if they are not.

# Example:

# grid = ["abc", "ade", "efg"]

# The grid is illustrated below:

# a b c
# a d e
# e f g

# The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer
# would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

# Trasposes a matrix:
def trasposeMatrix(m):
    m = [list(i) for i in zip(*m)]
    return m

def gridChallenge(grid):
    # Set default value:
    outValue = "YES"
    # Create and empty list
    tempList = []
    # The lists with normal list and sorted list:
    lists = [grid, tempList]

    # The original list is going to be processed twice:
    # First pass to sort rows, second pass to traspose,
    # sort and compare trasposed and sorted rows:
    for i in range(2):
        # Get current list:
        currentList = lists[i]
        # Traspose only on second pass:
        if (i == 1):
            currentList = trasposeMatrix(currentList)
        # Get number of rows:
        rows = len(currentList)

        # Process each row:
        for r in range(rows):
            # Get current row...
            currentRow = currentList[r]
            #... sort it alphabetically:
            tempRow = sorted(currentRow)

            # Store it on first pass:
            if (i == 0):
                tempList.append(tempRow)
            # Compare trasposed vs traposed sorted
            # on second pass:
            else:
                # Rows must match:
                if (currentRow != tempRow):
                    outValue = "NO"
                    # Stop list processing:
                    break
        else:
            continue
        break
    # Done:
    return outValue


# Test case entry:

grid = ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']
outValue = gridChallenge(grid)
print(outValue)