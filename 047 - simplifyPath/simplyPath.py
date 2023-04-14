# File        :   simplifyPath.py
# Version     :   1.0.0
# Description :   Solution to the simplifyPath problem
               
# Date:       :   Apr. 14, 2023
# Author      :   Mr. X
# License     :   Creative Commons CC0

# Given a string path, which is an absolute path (starting with a slash '/') to a file 
# or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a double 
# period '..' refers to the directory up a level, and any multiple consecutive slashes 
# (i.e. '//') are treated as a single slash '/'. For this problem, any other format of 
# periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:

# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target 
# file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.

# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.

# Example 2:
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level 
# is the highest level you can go.

# Example 3:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single 
# one.

def simplifyPath(path):
    # Split string:
    splittedString = path.split("/")
    # Ignore first char:
    splittedString = splittedString[1:]

    pathLenght = len(splittedString)

    # The string stack:
    pathStack = ["/"]

    for i, currentString in enumerate(splittedString):

        # Get stack length:
        stackLength = len(pathStack)

        # Check "..."
        if currentString == "..":
            # If stack elements > 1:
            if stackLength > 1:
                # Pop the last two entries:
                del pathStack[stackLength - 2:stackLength]
                # pathStack.pop()

        # Check "" empty string - a new "/
        elif currentString == "":
            continue
        # Ignore ".":
        elif currentString == ".":
            continue
        # Append current string:
        else:
            pathStack.append(currentString)
            pathStack.append("/")

    # Join string:
    pathStack = ''.join(pathStack)
    stringLength = len(pathStack)

    if stringLength > 1:
        # Remove last "/":
        pathStack = pathStack[:-1]

    return pathStack


# Test case entry:
path = "//a/./b///c/../../d"
print("in:", path)

newPath = simplifyPath(path)
print("out:", newPath)
