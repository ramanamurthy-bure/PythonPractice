'''

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
Language
Python 3

More
189101112131415
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if len(s)>0 and len(s) < 1000 :
        s1=[x.capitalize() for x in s.split(" ")]
        return " ".join(s1)

if __name__ == '__main__':
Line: 8 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if len(s)>0 and len(s) < 1000 :
        s1=[x.capitalize() for x in s.split(" ")]
        return " ".join(s1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
