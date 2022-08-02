'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.

'''


def minion_game(s1):
    # your code goes here
    import math
    import string
    substrgins = []
    s1 = s1.strip()
    Stuart = 0
    Kevin = 0
    voweletters = "AEIOU"

    if 0 < len(s1) <= math.pow(10, 6):
        for i in range(len(s1)):
            charval = s1[i]
            if charval not in voweletters:
                Stuart += (len(s1) - i)
            else:
                Kevin += (len(s1) - i)

        # print(Stuart)
        # print(Kevin)
        if Stuart > Kevin:
            return print("Stuart", Stuart)
        elif Stuart == Kevin:
            return print("Draw")
        else:
            return print("Kevin", Kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)