// File        :   numberPalindrome.cpp
// Version     :   1.0.0
// Description :   Solution to the numberPalindrome problem

// Date:       :   Mar 25, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// Given an integer x, return true if x is a palindrome integer. An integer is a palindrome when it reads 
// the same backward as forward. Do not convert the integer to string.

// Example:
// 121 is a palindrome while 123 is not.

#include <iostream>
#include <vector>

bool isPalindrome(int number) {
    // Check for non-negative:
    if ( number < 0 ){
        return false;
    }

    // Declare base variables:
    int d = number;
    // Individual digits will be stored here:
    std::vector<int> reverseDigits;

    // Split the input number in its digits:
    while( d != 0 ){
        // Get remainder:
        int current = d % 10;
        // Into the list:
        reverseDigits.push_back(current);
        // New integer position:
        d = d / 10;
    }

    // Create a vector with the original order:
    std::vector<int> digits{reverseDigits.rbegin(), reverseDigits.rend()};
    int totalDigits = (int)reverseDigits.size();

    // Loop through the individual digits and
    // check if reverse match the original digits:
    bool outValue = true;
    for ( int i = 0; i < totalDigits; i++ ) {
        int currentReverse = reverseDigits[i];
        int currendDigit = digits[i];
        // if no match, exit loop, return false
        if (currentReverse != currendDigit){
            outValue = false;
            break;
        }
    }

    // Done:
    return outValue;   
}

int main()
{
    // Set test case:
    int number = 92222229;

    // Compute result:
    bool outValue = isPalindrome(number);

    // Print result:
    std::cout<<std::to_string(outValue)<<std::endl;

    return 0;
}
