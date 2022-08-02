'''
Given
an
integer,, print
the
following
values
for each integer  from to:

Decimal
Octal
Hexadecimal(capitalized)
Binary
Function
Description

Complete
the
print_formatted
function in the
editor
below.

print_formatted
has
the
following
parameters:

int
number: the
maximum
value
to
print
Prints

The
four
values
must
be
printed
on
a
single
line in the
order
specified
above
for each  from to.Each value should be space-padded to match the width of the binary value of and the values should be separated by a single space.

Input
Format

A
single
integer
denoting.

Constraints

Sample
Input

17
Sample
Output

1
1
1
1
2
2
2
10
3
3
3
11
4
4
4
100
5
5
5
101
6
6
6
110
7
7
7
111
8
10
8
1000
9
11
9
1001
10
12
A
1010
11
13
B
1011
12
14
C
1100
13
15
D
1101
14
16
E
1110
15
17
F
1111
16
20
10
10000
17
21
11
10001
Language
Python
3

More
12345678910111213


def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b', ''))

    if (number >= 1 and number <= 99):
        for i in range(1, number + 1):
            a = str(int(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            b = str(oct(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            c = str(hex(i)).replace('0o', '').replace('0b', '').replace('0x', '').upper().rjust(w, ' ')
            d = str(bin(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            print(a, b, c, d)


if __name__ == '__main__':
    Line: 15
    Col: 23

Submit
Code

Run
Code

Upload
Code as File

Test
against
custom
input

'''


def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b', ''))

    if 1 <= number <= 99:
        for i in range(1, number + 1):
            a = str(int(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            b = str(oct(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            c = str(hex(i)).replace('0o', '').replace('0b', '').replace('0x', '').upper().rjust(w, ' ')
            d = str(bin(i)).replace('0o', '').replace('0b', '').replace('0x', '').rjust(w, ' ')
            print(a, b, c, d)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)