# File        :   infiniteSet.py
# Version     :   1.0.0
# Description :   Solution to the infiniteSet problem
#                
# Date:       :   Apr 25, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain 
# all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the 
# infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, 
# if it is not already in the infinite set.

# Example: 

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", 
# "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]

# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

class SmallestInfiniteSet(object):

    def __init__(self):
        # Init class variables:
        self.currentSmallest = 1
        self.lastMax = 1
        self.popList = {}

    # Finds the missing ascending key in a dictionary,
    # Which is totally not optimal LOL!
    def findKey(self, key, inputDict):
        keysList = list(inputDict.keys())
        keysList.sort()
        totalKeys = len(keysList)
        # Start at the given key:
        for i in range(key - 1, totalKeys, 1):
            currentKey = keysList[i]
            if currentKey != i + 1:
                # Return the missing key:
                return i + 1
        # All keys complete, return the 
        # next valid key in the list:
        return keysList[-1] + 1

    def popSmallest(self):
        # Pop current smallest:
        temp = self.currentSmallest
        print("Popping Element: " + str(temp), end=' ')

        # Check if not already popped:
        if temp not in self.popList:
            outValue = temp
            # Update current smallest:
            self.currentSmallest = self.currentSmallest + 1

        else:
            # outValue = temp + 1
            outValue = self.findKey(temp, self.popList)
            listMax = max(self.popList)
            print("Item already popped! -> Popping: " + str(outValue) + " [List Max]: " + str(listMax), end=' ')
            self.currentSmallest = outValue + 1

        # Goes into the popped list:
        self.popList[outValue] = 1

        # Get list size:
        listSize = len(self.popList)
        print("List Size: " + str(listSize), end=' ')

        # Update last max:
        if self.lastMax == outValue:
            self.lastMax = self.currentSmallest

        print("currentSmallest: " + str(self.currentSmallest), end=' ')
        print("lastMax: " + str(self.lastMax), end=' ')
        print("Popping List: " + str(self.popList))

        # Return popped item:
        return outValue

    def addBack(self, num):
        # Check it the number that needs to be back
        # has been popped before:
        if num in self.popList:
            print("Adding Back Element: " + str(num), end=' ')
            # Bring it back:
            del self.popList[num]

            # Get list size:
            listSize = len(self.popList)
            print("List Size: " + str(listSize), end=' ')

            # Update current smallest:
            # If list empty, reset both "pointers" to
            # the smallest element  (starting point)
            if listSize == 0:
                self.currentSmallest = 1
                self.lastMax = 1
            else:
                if num < self.currentSmallest:
                    self.currentSmallest = num

            print("currentSmallest: " + str(self.currentSmallest), end=' ')
            print("lastMax: " + str(self.lastMax), end=' ')
            print("Popping List: " + str(self.popList))
        else:
            print("Element not added. Already in the set: " + str(num))


# Test case entry. Watch the console for debugging status:
obj = SmallestInfiniteSet()
obj.addBack(6)
obj.addBack(1)

obj.popSmallest()  # Out: 1
obj.popSmallest()  # Out: 2

obj.addBack(1)
obj.addBack(1)

obj.popSmallest()  # Out: 1
obj.popSmallest()  # Out: 3
obj.popSmallest()  # Out: 4
obj.popSmallest()  # Out: 5

obj.addBack(1)

obj.popSmallest()  # Out: 1

obj.addBack(1)
obj.addBack(2)

obj.popSmallest()  # Out: 1
obj.popSmallest()  # Out: 2
obj.popSmallest()  # Out: 6

obj.addBack(2)

obj.popSmallest()  # Out: 2
obj.popSmallest()  # Out: 7

obj.addBack(5)
obj.addBack(1)
obj.addBack(3)
obj.addBack(2)
obj.addBack(2)

obj.popSmallest()  # Out: 1