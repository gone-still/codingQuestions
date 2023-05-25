// File        :   maxVowels.cpp
// Version     :   1.0.0
// Description :   Solution to the maxVowels problem

// Date:       :   May 22, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
// Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
// If it is not possible to buy both items, return -1.

// Given a string s and an integer k, return the maximum number of vowel letters 
// in any substring of s with length k.

// Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

// Example 1:
// Input: s = "abciiidef", k = 3
// Output: 3

// Explanation: The substring "iii" contains 3 vowel letters.


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
#include <map>
#include <map>


int maxVowels(std::string s, int k){

    // The dictionary of vowels:
    std::map<char, bool> vowelsDict;
    vowelsDict.emplace('a', true);
    vowelsDict.emplace('e', true);
    vowelsDict.emplace('i', true);
    vowelsDict.emplace('o', true);
    vowelsDict.emplace('u', true);

    int maxCount = 0;
    int vowelCount = 0;
    int stringLength = (int)s.size();

    // Loop through the input string
    for (int i=0; i<stringLength; i++){

        // Get current character:
        char currentChar = (char)s[i];
        // Check if it is vowel:
        bool isVowel = vowelsDict[currentChar];

        if (isVowel) {
            vowelCount++;
        }

        // window post-filling:
        if (i >= k){

            char firstChar = (char)s[i - k];
            bool isFirstVowel = vowelsDict[firstChar];
            if (isFirstVowel){
                vowelCount--;
            }

        }

        // Check max:
        if (vowelCount > maxCount){
            maxCount = vowelCount;
        }
    }

    return maxCount;

}

int main()
{
    // Set test case:
    std::string s = "singasong";
    int k = 4;
    int o = maxVowels(s, k);
    std::cout<<o<<std::endl;
    return 0;
}
