# File        :   validateStackSequence.py
# Version     :   1.0.0
# Description :   Solution to the validateStackSequence problem
               
# Date:       :   Apr. 13, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given two integer arrays pushed and popped each with distinct values, return true if this 
# could have been the result of a sequence of push and pop operations on an initially empty 
# stack, or false otherwise.

 
# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

def validateStackSequences(pushed, popped):
    # The temp stack:
    tempStack = []
    # Get lists lengths:
    pushedItems = len(pushed)
    poppedItems = len(popped)

    # If got an empty list, return false:
    if (pushedItems < 1) or (poppedItems < 1):
        return False

    i = 0  # push index
    j = 0  # pop index

    processItems = True
    pushItem = True
    popItem = False

    allPushed = False
    allPopped = False

    stackLength = -1

    # Process stack ops:
    while processItems:
        # Get pushed and popped:
        currentPushed = pushed[i]
        currentPopped = popped[j]

        # Pushed item goes into the stacK:
        if pushItem:
            tempStack.append(currentPushed)

        # Popped item goes outta the stack:
        if popItem:
            tempStack.pop()

        # Check number of stack elements:
        stackLength = len(tempStack)
        # Gotta need at least one item in the stack:
        if stackLength > 0:
            # Get stack item:
            currentStack = tempStack[stackLength - 1]

        # If current rear in stack equals current element to
        # be popped...:
        if currentStack == currentPopped:
            # Pop element, if the are still elements to
            # be popped:
            if not allPopped:
                pushItem = False
                popItem = True
                # Increase pop list index:
                if j < poppedItems - 1:
                    j = j + 1
                # Check if index reached the end of
                # the items to be poped list:
                if j == poppedItems - 1:
                    print("All popped!")
                    allPopped = True
            else:
                # There are no more elements to be popped,
                # end the algorithm:
                print("No more pop items.")
                processItems = False
        else:
            # Push items, but items need to be pushed
            # in need to be there first:
            if not allPushed:
                pushItem = True
                popItem = False
                # Increase push list index:
                if i < pushedItems - 1:
                    i = i + 1
                # Check if index reached the end of
                # the items to be pushed list:
                if i == pushedItems - 1:
                    print("All pushed!")
                    allPushed = True
            else:
                # There are no more elements to be pushed,
                # end the algorithm:
                print("No more push items.")
                processItems = False

    # Set output value
    outValue = True
    # At this point, either the stack must be empty
    # or containing the last element that wasn't pop
    # in the last iteration:
    if stackLength > 1:
        outValue = False

    # Print the stack:
    print(tempStack)
    # Done:
    return outValue


# Test case entry:
pushed = [1, 2, 4, 5, 3]
popped = [1, 2, 5, 3, 4]

isValid = validateStackSequences(pushed, popped)
print(isValid)
