"""The way we’ll simulate this is to write a function that
generates a string that is 28 characters long by choosing
random letters from the 26 letters in the alphabet plus the space.

We’ll write another function that will score each generated string
by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score,
then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.
To make it easier to follow your program’s progress this
third function should print out the best string generated
so far and its score every 1000 tries."""

import random

def monkey():
    # returns the result of a monkey writing 28 random letters
    
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alphabetLength = len(alphabet)
    result = ''
    randomNum = 0
    for i in range(28):
        randomNum = random.randint(0, alphabetLength - 1)
        result += alphabet[randomNum]

    return result

def score(monkeySaid):
    # returns the percentage score of how close the monkey got to the target
    
    target = "methinks it is like a weasel"
    accuracy = 0
    targetList = list(target)
    monkeyList = list(monkeySaid)

    for i in range(len(targetList)):
        if (monkeyList[i] == targetList[i]):
            accuracy += 3.57

    
    return accuracy    

def guess(accuracy):
    # continously calls score until the monkey gets it right
    # prints the best result every 1000 guesses
    
    i = 0
    
    while (accuracy < 99):
        i += 1
        score(monkey())
        print(accuracy)
        print(i)
        if (i == 1000):
            print(accuracy)

score(monkey())
guess(score(monkey()))
