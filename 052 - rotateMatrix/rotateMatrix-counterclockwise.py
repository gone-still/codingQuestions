# File        :   rotateMatrix-counterclockwise.py
# Version     :   1.0.0
# Description :   Solution to the rotateMatrix problem
#                
# Date:       :   May 24, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given an n x n 2D matrix representing an image, rotate the 
# image by 90 degrees (counter clockwise).

# You have to rotate the image in-place, which means you have to modify 
# the input 2D matrix directly. DO NOT allocate another 2D matrix and 
# do the rotation.

# Example:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[3,6,9],[2,5,8],[1,4,7]]


def rotateMat(mat):
    # Get mat dimensions:
    cols = len(mat)
    rows = cols

    # Loop through mat "diagonally":
    for j in range(rows):
        for i in range(0, j + 1):
            # Get values:
            g = mat[i][j]
            r = mat[j][i]
            # Swap values:
            mat[i][j] = r
            mat[j][i] = g

    # Swap rows:
    totalSwaps = rows // 2
    for m in range(totalSwaps):
        # Get rows:
        firstRow = mat[m]
        lastRow = mat[(rows - 1) - m]

        # Swap rows:
        mat[m] = lastRow
        mat[(rows - 1) - m] = firstRow


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotateMat(mat)
print("Out:", mat)
