# File        :   rotateMatrix-clockwise.py
# Version     :   1.0.0
# Description :   Solution to the rotateMatrix problem
#                
# Date:       :   Apr 24, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given an n x n 2D matrix representing an image, rotate the 
# image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify 
# the input 2D matrix directly. DO NOT allocate another 2D matrix and 
# do the rotation.

# Example:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):
    # Matrix size (cols and rows):
    n = len(matrix)
    # Swap values along the diagonal...
    # Movement is like in a stair, swapping
    # elements at every step:
    for y in range(n):
        for x in range(0, y + 1):
            tempVal = matrix[y][x]
            matrix[y][x] = matrix[x][y]
            matrix[x][y] = tempVal

    # Reverse columns along the center:
    m = n // 2  # Number of "movements" along the x-axis (columns to be swapped) -> sides to center
    for x in range(m):
        for y in range(n):
            # Get extreme values (left and right)
            # and swap them:
            tempVal = matrix[y][x]
            colIndex = (n - 1) - x
            matrix[y][x] = matrix[y][colIndex]
            matrix[y][colIndex] = tempVal

    pass

# Test case entry:
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix)
print("out:", matrix)
