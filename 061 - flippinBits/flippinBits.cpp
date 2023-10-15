// File        :   flippinBits.cpp
// Version     :   1.0.0
// Description :   Solution to the flippinBits problem

// Date:       :   Jun 06, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// Given 3 positives numbers a, b and c. Return the minimum flips required in some
// bits of a and b to make ( a OR b == c ). (bitwise OR operation).
// Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 
// in their binary representation.

// Example 1:
// Input: a = 2, b = 6, c = 5
// Output: 3
// Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)


#include <iostream>
#include <bitset> // bit representation & manipulation

int minFlips(int a, int b, int c){

    // Cast ints to 32-bit words :
    std::bitset<32> aInt = (std::bitset<32>)a;
    std::bitset<32> bInt = (std::bitset<32>)b;
    std::bitset<32> cInt = (std::bitset<32>)c;

    int maxCount = 0;

    // Loop through the 32-bit word:
    for (int i = 0; i < 32; i++){
        // Get individual bits:
        int aBit = aInt[i];
        int bBit = bInt[i];
        int cBit = cInt[i];

        // Check OR truth table:
        if (cBit == 0){
            if (aBit != 0){
                maxCount++;
            }
            if (bBit != 0){
                maxCount++;
            }
        }else{
            if (aBit == 0 && bBit == 0){
                maxCount++;
            }
        }

    }

    return maxCount;

}

int main()
{
    // Set test case:
    int a = 4;
    int b = 2;
    int c = 7;

    int o = minFlips(a, b, c);

    std::cout<<o<<std::endl;

    return 0;
}
