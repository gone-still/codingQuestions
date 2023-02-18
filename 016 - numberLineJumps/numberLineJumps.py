# File        :   numberLineJumps.py
# Version     :   1.0.0
# Description :   Solution to the numberLineJumps problem
#                
# Date:       :   Feb 17, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# You are choreographing a circus show with various animals. For one act, you are given 
# two kangaroos on a number line ready to jump in the positive direction 
# (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time 
# as part of the show. If it is possible, return YES, otherwise return NO.

# Example:
# x1 = 2, v1 = 1
# x2 = 1, v2 = 2
# After one jump, they are both at 3, so the answer is YES.

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Default value is "NO":
    outString = "NO"
    
    # Ends must be the same, so the number of
    # jump is computed as:
    # totalJumps = (x2 - x1)/(v1 - v2) 
    
    # Check denominator for possible division
    # by zero:
    num = (x2 - x1)
    den = (v1 - v2)
    
    # Check denominator:
    if (den > 0):   
        # Compute total of jumps: 
        totalJumps = (x2 - x1)/(v1 - v2)  
        
        # Check if the total jumps are integer jumps:      
        totalJumpsDiff = totalJumps - int(totalJumps)
        epsilon = 0.0001
        
        # Number of jumps must be >= 0 and integer:
        if ( totalJumps >= 0 ) and ( totalJumpsDiff < epsilon ):
            outString = "YES"
    
    # Done:
    return outString

# Test case entry:
if __name__ == '__main__':

    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    result = kangaroo(x1, v1, x2, v2)

    print(result)

