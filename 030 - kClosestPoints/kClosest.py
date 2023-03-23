# File        :   kClosest.py
# Version     :   1.0.0
# Description :   Solution to the kClosest problem
#
# Date:       :   Mar 22, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]

# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

def kClosest(points, k):
    # Output points are stored here:
    outPoints = []
    # Function variables:
    origin = (0, 0)
    totalPoints = len(points)

    # Loop through the list of points, get each one
    # and compute its distance to the origin.
    # Store the data in the outPoints list:
    for p in range(totalPoints):
        currentPoint = points[p]
        dx = origin[0] - currentPoint[0]
        dy = origin[0] - currentPoint[1]

        # Get distance of current point to origin:
        d = pow(dx, 2.0) + pow(dy, 2.0)
        # Into the list:
        outPoints.append((d, currentPoint))

    # Sort list based on distance (element 0 of the tuple):
    outPoints = sorted(outPoints, key=lambda tup: tup[0])
    # Extract the k points from the list of tuples:
    outPoints =  list(zip(*outPoints[0:k]))[1]

    # Done:
    return outPoints

# Test case entry:
points = [[3, 3], [-2, 4], [6, 6], [5, -1]]
k = 2
# Get and print the result:
outPoints = kClosest(points, k)
print(outPoints)