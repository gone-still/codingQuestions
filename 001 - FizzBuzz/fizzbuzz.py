# File        :   fiizbuzz.py
# Version     :   1.0.0
# Description :   Solution to the fizzbuzz problem
#                
# Date:       :   Jan 30, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a number n, for each integer i in the range from 1 to n inclusive, print one value 
# per line as follows:

# if i is a multiple of both 3 and 5, print FizzBuzz
# if i is a multiple of 3 (but no 5), print Fizz
# if i is a multiple of 5 (but no 3), print Buzz
# if i is not a multiple of 3 or 5, print the value of ii

import math
import os
import random
import re
import sys

def fizzBuzz(n):

    # Loop through the numbers:
    for i in range(1, n + 1, 1):
        
        # Setup conditions:
        aTest = i%3 == 0
        bTest = i%5 == 0

        # Test the conditions:
        if aTest:
            if bTest:
                print("FizzBuzz")
            else:
                if not(bTest):
                    print("Fizz")
        else:
            if bTest:
                print("Buzz")
            else:
                print(i)


if __name__ == '__main__':
    n = 15
    fizzBuzz(n)