// File        :   countingValleys.cpp
// Version     :   1.0.0
// Description :   Solution to the countingValleys problem

// Date:       :   Mar 14, 2023
// Author      :   Mr. X
// License     :   Creative Commons CC0

// An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly s steps, 
// for every step it was noted if it was an uphill U or a downhill D step. Hikes always start and end at 
// sea level, and each step up or down represents a  unit change in altitude. 

// We define the following terms:

// A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level 
// and ending with a step down to sea level.

// A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level 
// and ending with a step up to sea level.

// Given the sequence of up and down steps during a hike, find and print the number of valleys walked 
// through.

// Example

// s = 8
// path = [DDUUUUDD]

// The hiker first enters a valley  units deep. Then they climb out and up onto a mountain 2 units 
// high. Finally, the hiker returns to sea level and ends the hike.

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


int main()
{

    std::string hikePath = "UDDDUDUU";

    int previousCode = 0; 
    int codeAccumulator = 0;
    int totalValleys = 0; 
    int totalMountains = 0;

    std::string::iterator  it;

    // Loop thru the path, getting each string character
    // at a time:
    for (it = hikePath.begin(); it != hikePath.end(); it++){
    	
    	// Get current char from string:
        char currentChar = *it;

        // Check if 'U' or 'D':
        if ( currentChar == 'D' ){
            std::cout<<"Found downhill"<<std::endl;
            // Decrease step accumulator
            codeAccumulator = codeAccumulator - 1;
        }else{
            if ( currentChar == 'U' ){
                std::cout<<"Found uphill"<<std::endl;
                // Increase step accumulator:
                codeAccumulator = codeAccumulator + 1;
            }
        }

        // Check zero cross:
        if ( (previousCode != 0) && (codeAccumulator == 0) ){

            int codeDifference = previousCode - codeAccumulator;
            std::cout<<"codeDifference: "<<codeDifference<<std::endl;

            // Was it a valley?
            if ( codeDifference < 0 ){ 	// Cross came from negative number
                std::cout<<"Found valley"<<std::endl;
                totalValleys++;
            }else{ 					 	// Cross came from positive number:
                std::cout<<"Found mountain"<<std::endl;
                totalMountains++;
            }

        }

        // Assign previous code:
        previousCode = codeAccumulator;

    }

    // Done:
    std::cout<<"[final] Valleys: "<<totalValleys<<std::endl;
    std::cout<<"[final] Mountains: "<<totalMountains<<std::endl;

    return 0;
}
