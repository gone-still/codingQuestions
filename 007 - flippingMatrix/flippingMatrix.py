# File        :   flippingMatrix.py
# Version     :   1.0.0
# Description :   Solution to the flippingMatrix problem
#                
# Date:       :   Feb 06, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. 
# He can reverse any of its rows or columns any number of times. The goal of the game is to 
# maximize the sum of the elements in the n x n submatrix located in the upper-left quadrant of the matrix.

# Given the initial configurations for q matrices, help Sean reverse the rows and columns of 
# each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is 
# maximal.

# Example: m = [[1, 2], [3, 4]]

# The maximal sum is 4 and the problem is pretty badly redacted.


def flippingMatrix(matrix):

    # Get matrix dimensions:
    matrixRows = len(matrix)
    matrixCols = len(matrix[0])

    # Get middle of the matrix
    halfRows = matrixRows // 2
    halfCols = matrixCols // 2

    # Accumulate max numbers here:
    maxCum = 0

    # Loop through the matrix:
    for j in range(halfRows):
        for i in range(halfCols):

            # Get row elements:
            a = matrix[j][i] # row first element
            b = matrix[j][(matrixCols - 1) - i] # row last element

            # Get col elements:
            c = matrix[(matrixRows - 1) - j][i] # col last element
            d = matrix[(matrixRows - 1) - j][(matrixCols - 1) - i] # last row, last col element

            # Get max:
            currentMax = max(a, b, c, d)
            
            # Accumulate current max to history:
            maxCum = maxCum + currentMax

    # Done:
    return maxCum


if __name__ == '__main__':
    arr = [[112, 42, 83, 119],
           [56, 125, 56, 49],
           [15, 78, 101, 43],
           [62, 98, 114, 108]]

    result = flippingMatrix(arr)

    print(result)
