# File        :   caesarCipher.py
# Version     :   1.0.0
# Description :   Solution to the caesarCipher problem
#                
# Date:       :   Feb 03, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past 
# the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

# Example:

# k = 3
# s = "There's-a-starman-waiting-in-the-sky"

# The alphabet is rotated by 3, matching the mapping above. 
# The encrypted string is: Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb

# Note: The cipher only encrypts letters; symbols such as - 
# remain unencrypted.

def caesarCipher(s, k):
    
    # Set the alphabet dictionary. Every key is a character and its value its "index":
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22,
                "x": 23, "y": 24, "z": 25}

    # Set the alphabet list. Every indexed item is a character:
    alphabetList = list(alphabet)

    # Containers' lengths:
    alphabetLength = len(alphabet)
    stringLength = len(s)
    
    # Upper case flag:
    isUpper = False

    # The out string:
    outString = ""

    # Loop through the input string:
    for c in range(stringLength):

        # Get current char from input:
        currentChar = s[c]

        # Check case:
        if (currentChar.isupper()):
            isUpper = True

        # Convert to lower:
        currentChar = currentChar.lower()

        # Check if entry exists in dictionary:
        if (currentChar in alphabet):

            # Get its index:
            charIndex = alphabet[currentChar]
            # Add index + rotation factor:
            charIndex = charIndex + k

            # Set new char index:
            # Every 26 characters is a new "start" in the dictionary:
            newIndex = charIndex - alphabetLength * int(charIndex / alphabetLength)
            currentChar = alphabetList[newIndex]

            # Convert back to upper case if the flag was set:
            if (isUpper):
                currentChar = currentChar.upper()
                isUpper = False
        
        # All in one big-ass striing:
        outString = outString + currentChar
        
    # Done:
    return outString


if __name__ == '__main__':

    # Rotation Factor:
    k = 3

    # Input String:
    s = "There's-a-starman-waiting-in-the-sky"

    # Encrypt the strring:
    encryptedString = caesarCipher(s, k)

    # Print it:
    print(encryptedString)
