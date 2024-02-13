# File        :   longestValidParentheses.py
# Version     :   1.0.0
# Description :   Solution to the Longest Valid Parentheses problem
#
# Date:       :   Feb 12, 2024
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed)
# parentheses substring
#
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0

from collections import deque


def longestValid(inputString: str) -> int:
    """
    :param inputString: the input string
    :return: max length of valid parentheses
    """
    # Set the queues:
    stack = deque()
    indices = deque()

    # Set the max length found so far,
    # and the max length in the entire string
    currentLength = 0
    maxLength = 0

    # Last character from string is stored here:
    last = ""

    # Part 1 - Get a queue with the indices of the
    # unbalanced parenthesis

    # Loop thru string:
    for i, current in enumerate(inputString):
        # Get current stack length, if items stored
        # in stack, get the latest pushed:
        stackLength = len(stack)
        if stackLength > 0:
            last = stack[-1]

        # Append current character and its position
        # (index) in the input string:
        stack.append(current)
        indices.append(i)

        # Check pop condition: () -> current: ")" and
        # last: "(":
        if current == ")" and last == "(":
            # Count 2 symbols (opening and closing par):
            currentLength += 2
            # Pop 2 symbols:
            stack.pop()
            stack.pop()
            # Pop 2 indices:
            indices.pop()
            indices.pop()
            # Reset last stored char:
            last = ""

        else:
            # Check a lone "(" to end the current
            # length counter:
            if last == "" and current == ")":
                # Reset variables:
                currentLength = 0
                stack.pop()
                last = ""

        # Store longest count so far:
        maxLength = max(maxLength, currentLength)

    # Part 2 - If there are multiple unbalanced parentheses
    # in the stack, look for the largest count of valid symbols:

    # Stack has unbalanced items:
    if len(stack) > 0:

        # Set index that loops through the elements
        # of the indices queue:
        k = 0
        # Set current and max counter lengths:
        currentLength = 0
        maxLength = 0
        stringLength = len(inputString)

        # Append an extra element, which indicates
        # "End of Stack":
        indices.append(stringLength)

        # The indices queue has the indices of the
        # unbalanced parentheses, each of these numbers
        # indicate a new "valid" string of parentheses.
        # Accumulate its length until a new index is found:
        for j in range(stringLength + 1):
            # Get current index limit from the queue:
            currentLimit = indices[k]
            # If the current position of the string is
            # different to the current limit, accumulate
            # the "valid" string length:
            if currentLimit != j:
                currentLength += 1

            # Break up the accumulation on every index and 
            # just after the last char of the input string:
            else:
                # Get max length so far:
                maxLength = max(maxLength, currentLength)
                # Reset accumulator:
                currentLength = 0
                # On to the next limit index (if queue
                # allows it):
                if len(indices) > 1:
                    k += 1

    # Done:
    return maxLength


s = "()()())))))))()()()(((((((((((("
maxLength = longestValid(s)
print("Max Length:", maxLength)
