// File        :   electronicsShop.cpp
// Version     :   1.0.0
// Description :   Solution to the electronicsShop problem

// Date:       :   Feb 28, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
// Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
// If it is not possible to buy both items, return -1.

// Example:
// b = 60
// keyboards = [40, 50, 60]
// drives = [5, 8, 12]

// The person can buy a 40 keyboard + 12 drive = 52, or a 50 keyboard + 8 drive = 58.
// Choose the latter as the more expensive option and return 58.

// Input Types:
// int keyboards[n]: the keyboard prices
// int drives[m]: the drive prices
// int b: the budget

// Output Types:
// int: the maximum that can be spent, or -1 if it is not possible to buy both items

#include <iostream>
#include <vector>
#include <algorithm>

int getMoneySpent(std::vector<int> keyboards, std::vector<int> drives, int budget) {

    // Sort vectors from largest to smallest item:
    std::sort(keyboards.begin(), keyboards.end(), std::greater<int>());
    std::sort(drives.begin(), drives.end(), std::greater<int>());

    // Get sizes of vectors:
    int totalKeyboards = (int)keyboards.size();
    int totalDrives = (int)drives.size();

    float outValue = -1.00;

    // Loop through current and target vectors to
    // get total product sum:
    for (int k = 0; k < totalKeyboards; k++) {

        // Get current keyboard:
        int currentKeyboard = keyboards[k];

        // Check if this price is smaller than the budget:
        if (currentKeyboard <= budget) {

            // Sum with current drive:
            for (int b = 0; b < totalDrives; b++) {

                // Get current drive:
                int currentDrive = drives[b];
                // Compute sum:

                float priceSum = currentKeyboard + currentDrive;

                // Check if current sum is below budget and it is
                // maximum so far:
                if ( (priceSum <= (float)budget) && (priceSum >= outValue) ) {

                    // Set result to current max sum:
                    outValue = priceSum;
                }
            }
        }
    }

   // The instructions demanded to return an int...
   return (int)outValue;
}

int main()
{
    // Set test case:
    int b = 60;
    std::vector<int> keyboards = {40, 50, 60};
    std::vector<int> drives = {5, 8, 12};

    // Compute result:
    int maxMoneSpent = getMoneySpent(keyboards, drives, b);

    // Print result:
    std::cout<<maxMoneSpent<<std::endl;

    return 0;
}
