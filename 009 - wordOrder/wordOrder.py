# File        :   wordOrder.py
# Version     :   1.0.0
# Description :   Solution to the wordOrder problem
#                
# Date:       :   Feb 10, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given n words. Some words may repeat. For each word, output its 
# number of occurrences. The output order should correspond with the input 
# order of appearance of the word.  See the sample input/output for 
# clarification.
# Note: Each input line ends with a "\n" character.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output

# 3
# 2 1 1

# Explanation:
# There are 3 distinct words. Here, "bcdef" appears twice in the input at the first 
# and last positions. The other words appear once each. The order of the first 
# appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

# Word list:
s = [ "bcdef", "abcdefg", "bcde", "bcdef" ]

# Get list size:
n = len(s)

# Prepare the dictionary of words:
wordDictionary = {}

# Loop thorugh the words list:
for i in range(n):
    # Get target string:
    targetString = s[i]
    # Check if a dictionary key for this
    # string exists:
    if targetString in wordDictionary:
        # Increase string count by 1:
        wordDictionary[targetString] += 1
    else:
        # First entry in dictionary:
        wordDictionary[targetString] = 1

# Print the different words found:
differentWords = len(wordDictionary)
print(differentWords)

# Print word occurrences:
outString = ""
for i in wordDictionary:
    # Get dict value:
    currentValue = wordDictionary[i]
    # Concatenate each value in a big-ass string:
    outString = outString + str(currentValue) + " "

# Print the string of word occurrences:
print(outString)