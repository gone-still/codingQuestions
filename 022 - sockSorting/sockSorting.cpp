// File        :   sockSorting.cpp
// Version     :   1.0.0
// Description :   Solution to the sockSorting problem

// Date:       :   Mar 02, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// Given a vector of sock colors, determine how many pairs of one color are and
// how many single socks of one color exist. Do not use dictionaries.


// Example:
// sockColors = [ 1, 2, 1, 2, 1, 3, 2, 3 ]
// There are 3 pairs of socks and 2 singles.


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    // Set vector of sock colors:
    std::vector<int> sockColors = { 1, 2, 1, 2, 1, 3, 2, 3 };
    // Counter variables:
    int sockPairs = 0; int sockSingles = 0;

    // Loop through the vector and pick a target item:
    for (int i = 0; i < (int)sockColors.size(); i++){
        
        // Get current item (sock color):
        int currentColor = sockColors[i];
        std::cout<<"i: "<<i<<" currentColor: "<<currentColor<<std::endl;

        // Check if the item is unprocessed:
        if ( currentColor != -1 ){

            // Loop thru targets:
            for ( int j = 0 ; j < (int)sockColors.size(); j++ ){
                
                std::cout<<"j: "<<j<<std::endl;
                int targetColor = sockColors[j]; //get target
                std::cout<<"targetColor: "<<targetColor<<std::endl;
                
                // Make sure to process to process different items:
                if ( j != i ){
                    // Get unprocessed colors:
                    if ( targetColor != -1 ){
                        // Check if this is a pair:
                        if ( currentColor == targetColor ){
                            std::cout<<"Found Pair -> "<<i<<", "<<j<<std::endl;
                            // IIncrease pair count:
                            sockPairs++;
                            // Mark processed items:
                            sockColors[ i ] = -1;
                            sockColors[ j ] = -1;
                            // Exit loop:
                            j = (int)sockColors.size();
                        }
                    }

                }

                // Check if this is a single item...
                if ( j == (int)sockColors.size()-1 ){
                    std::cout<<"Found Single -> "<<i<<std::endl;
                    // Increase single count:
                    sockSingles++;
                    // Mark item:
                    sockColors [ i ] = -1;
                }
            }
        }

        // Checck out the data so far:
        std::cout<<"Pairs: "<<sockPairs<<std::endl;
        std::cout<<"Singles: "<<sockSingles<<std::endl;
    }

    // Check the final data:
    std::cout<<"[final] Pairs: "<<sockPairs<<std::endl;
    std::cout<<"[final] Singles: "<<sockSingles<<std::endl;

    return 0;
}
