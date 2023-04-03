# File        :   rescueBoats.py
# Version     :   1.0.0
# Description :   Solution to the rescueBoats problem
#                
# Date:       :   Apr 02, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given an array people where people[i] is the weight of the ith person, and an infinite 
# number of boats where each boat can carry a maximum weight of limit. Each boat carries at most 
# two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.


# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

def numRescueBoats(self, people, limit):
    # Sort the list of people:
    people.sort()
    # Get total people:
    totalPeople = len(people)

    # Indices:
    i = 0 # Start of the list
    j = totalPeople - 1 # End of the list:

    boats = 0

    # until the indices change positions:
    while i <= j:
        # Get current limit:
        currentLimit = people[i] + people[j]
        # Check if the two persons are under the limit:
        if  currentLimit<= limit:
            # Increase smallest element index:
            i += 1 

        # Decrese largest element index:
        j -= 1
        # Boat count goes up by one:
        boats += 1
        
    # Done
    return boats