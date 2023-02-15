# File        :   noIdea.py
# Version     :   1.0.0
# Description :   Solution to the noIdea problem
#                
# Date:       :   Feb 14, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# There is an array of n integers. There are also two disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B . Your initial happiness is 0. 
# For each i integer in the array, if i belongs to A, you add +1 to your happiness. 
# If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. 
# Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. 
# However, the array might contain duplicate elements.

# Get input array and its length:
r = [1, 5, 3]
n = len(r)

# Get A and B and their length:
a = [3, 1]
b = [5, 7]
m = len(a)

# Convert a and b to dictionaries:
aDict = dict.fromkeys(a, True)
bDict = dict.fromkeys(b, True)

# Set total happiness:
totalhappiness = 0

# Loop through the target array:
for i in range(n):
    # Get current item, which is the key
    # to the A and B dictionaries:
    currentKey = r[i]
    # Check in A:
    if currentKey in aDict:
        totalhappiness   +=1
    else:
        # Check in B:
        if currentKey in bDict:
            totalhappiness  -= 1

# Done:
print(totalhappiness )