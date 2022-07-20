'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
Language
Pypy 2

More
12345678910111213141516
def swap_case(s):
    lenofstr = len(s)
    new_str = ""
    if lenofstr>0 and lenofstr <=1000:
        for x in s:
            if x.isupper():
                new_str = new_str + x.lower()
            elif x.islower():
                new_str = new_str + x.upper()
            else:

Line: 1 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
'''

def swap_case(s):
    lenofstr = len(s)
    new_str = ""
    if lenofstr>0 and lenofstr <=1000:
        for x in s:
            if x.isupper():
                new_str = new_str + x.lower()
            elif x.islower():
                new_str = new_str + x.upper()
            else:
                new_str = new_str + x
    else:
        print("Invalid Input")
    return new_str

if __name__ == '__main__':
    s="Ramana"
    swap_case(s)