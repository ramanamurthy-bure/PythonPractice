'''
This tool returns  length subsequences of elements from the input iterable allowing individual elements to
 be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination
tuples will be produced in sorted order.

Example:
from itertools import combinations_with_replacement
print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
A = [1,1,3,3,3]
print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
Task

You are given a string .
Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.
Constraints
0<k<len(S)

The string contains only UPPERCASE characters.
Output Format
Print the combinations with their replacements of string  on separate lines.
Sample Input
HACK 2
Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, size = input().split(" ")
lenval = len(s)
size = int(size)
if 0 < size <= lenval:
    print(*["".join(x) for x in combinations_with_replacement(sorted(s), size)], sep='\n')
