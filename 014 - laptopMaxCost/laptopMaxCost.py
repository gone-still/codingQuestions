# File        :   wordOrder.py
# Version     :   1.0.0
# Description :   Solution to the wordOrder problem
#                
# Date:       :   Feb 10, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# A company manufactures a fixed number of laptops every day. However, if some defect is encountered during the testing of a laptop, 
# it is labeled as "illegal" and is not counted in the laptop count of the day. 

# Given the cost to manufacture each laptop, its label as "illegal" or "legal", and the number of legal laptops to be manufactured 
# each day, find the maximum cost incurred by the company in a single day in manufacturing all the laptops.

# Note that if a laptop is labeled as illegal, its manufacturing cost is still incurred by the company, even though it is not 
# included in the laptop count. 

# Also, days are only taken into when the daily laptop count has been completely met. If there are no such days, the answer is 0.

# For example, let's say there are n = 5 laptops, where cost = [2,5, 3, 11, 1]. 
# The labels for these laptops are labels = ["legal", "illegal", "legal", "illegal", "legal"). 
# Finally, the daily Count = 2, which means that the company needs to manufacture 2 legal laptops each day. 

# The queue of laptops can be more easily viewed as follows:

# cost 2, "legal" 
# cost 5, "illegal" 
# cost 3, "legal" 
# cost 11, "illegal" 
# cost 1, "legal"

# On the first day, the first three laptops are manufactured in order to reach the daily count of 2 legal laptops. 
# The cost incurred on this day is 2 + 5 + 3 = 10. 
# On the second day, the fourth and fifth laptops are manufactured, but because only one of them is legal, 
# the daily count isn't met, so that day is not taken into consideration. 

# Therefore, the maximum cost incurred on a single day is 10.

def maxCost(cost, labels, dailyCount):
    # Prepare the list of temp results:
    results = []
    # Get size of the cost list:
    listSize = len(cost)

    # Total cost accumulation + 
    # label count variables:
    totalCost = 0
    labelCount = 0

    # Loop through the list of costs:
    for i in range(listSize):
        # Get cost:
        currentCost = cost[i]
        # Get label:
        currentLabel = labels[i]
        # Accumulate costs:
        totalCost = totalCost + currentCost

        # Check label:
        if (currentLabel == "legal"):
            # If legal, increase label count 
            # by 1
            labelCount += 1
            # Check if the daily quota has
            # been reached:
            if (labelCount == dailyCount):
                # Current total cost goest into
                # the results list:
                results.append(totalCost)
                # Clear counters:
                labelCount = 0
                totalCost = 0

    # Get max from the list, if no items, the
    # default return value is "0":
    totalMaxCost = max(results, default=0)

    # Done:
    return totalMaxCost

# Test case entry point:
cost = [2, 5, 3, 11, 1]
labels = ["legal", "illegal", "legal", "illegal", "legal"]
dailyCount = 2

outcost = maxCost(cost, labels, dailyCount)

print(outcost)