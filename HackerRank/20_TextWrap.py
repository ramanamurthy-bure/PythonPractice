'''
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Language
Python 3

More
1234567891011121314151617
import textwrap

def wrap(string, max_width):
    len_of_string = len(string)

    if (len_of_string>0 and len_of_string<1000) and ((max_width>0 and max_width<len_of_string)):
        count_val = 0
        wraptext=""
        for x in string:

Line: 2 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input

'''

import textwrap


def wrap(string, max_width):
    len_of_string = len(string)

    if (len_of_string > 0 and len_of_string < 1000) and ((max_width > 0 and max_width < len_of_string)):
        count_val = 0
        wraptext = ""
        for x in string:
            wraptext += x
            count_val += 1
            if count_val == max_width:
                count_val = 0
                wraptext += '\n'
    return wraptext


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)