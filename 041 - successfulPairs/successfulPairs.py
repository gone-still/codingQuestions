# File        :   successfulPairs.py
# Version     :   1.0.0
# Description :   Solution to the successfulPairs problem
#
# Date:       :   Apr 01, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are given two positive integer arrays spells and potions, of length n and m respectively, where 
# spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of 
# their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a 
# successful pair with the ith spell.

# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]

# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.

# Thus, [4,0,3] is returned.
 
def successfulPairs(spells, potions, success):

    # Create a copy of spells with original item index:
    sortedSpells = [(potion, index) for index, potion in enumerate(spells)]
    # Sort spell list based on spell:
    sortedSpells = sorted(sortedSpells, key=lambda tup: tup[0])
    # Sort potions:
    potions.sort()

    # Get lists lengths:
    totalSpells = len(sortedSpells)
    totalPotions = len(potions)

    # potion indexing starts at the end of the list:
    potionIndex = totalPotions - 1

    pairsList = [0] * totalSpells
    successCounter = 0

    # Loop through the spells lists, get each spell and test it
    # with each potion, starting from the end of the potion list.

    # if both lists are sorted, and the smallest spell multiplied
    # with the biggest potion is at least equal to the min success
    # factor, then, all following spells for that potion will be
    # accepted. So, we only traverse the potion list from end to
    # start one time. Be sure to accumulate the number of successful
    # combinations!

    for s in range(totalSpells):

    	# Get current spell & potion:
        currentSpell = sortedSpells[s][0]
        spellIndex = sortedSpells[s][1]

        processPotion = True

        # Traverse the potions list just one time, while
        # there are successfull combinations of spells * potions:
        while (processPotion):

            # Get biggest element from potions list:
            currentPotion = potions[potionIndex]
            # Get current success:
            currentSucess = currentSpell * currentPotion

            # Check if the potions index is positive and current success
            # factor is >= that the minimum:
            if (potionIndex >= 0) and (currentSucess >= success):
                potionIndex -= 1 # from end to start
                successCounter += 1 # accumulate this, for each succesful pair
            else:
                processPotion = False

        # Store count into appropiate index
        # in out list:
        pairsList[spellIndex] = successCounter

    return pairsList


# Test case entry:
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
pairs = successfulPairs(spells, potions, success)
print(pairs)
