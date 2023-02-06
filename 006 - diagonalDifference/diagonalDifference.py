# File        :   diagonalDifference.py
# Version     :   1.0.0
# Description :   Solution to the diagonalDifference problem
#                
# Date:       :   Feb 05, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Example: 

# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal: 1 + 5 + 9 = 15
# The right to left diagonal: 3 + 5 + 9 = 17

# Their absolute difference is: abs(15 - 17) = 2


def diagonalDifference(arr):

    # Get matrix dimensions:
    rows = len(arr)
    cols = len(arr[0])

    # Store cumulative sums here:
    sums = [0, 0]

    # Matrix indices, left and right indexing:
    right = 0
    left = cols - 1

    # Loop through the matrix rows:
    for j in range(rows):

        # Right element:
        f = arr[j][right]
        sums[0] = sums[0] + f

        # Left element:
        s = arr[j][left]
        sums[1] = sums[1] + s

        # Adjust indices:
        right += 1
        left -= 1

    # Compute final absolute difference:
    absDifference = abs(sums[0] - sums[1])

    # Done:
    return absDifference



if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)

    print(result)
