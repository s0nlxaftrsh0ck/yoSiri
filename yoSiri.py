# App: yoSiri
# Description: A bot to create randomized questions to ask Siri
# Author: Ronald Pusey
# Create Date: 5/9/2022
# Version: 0.0.3 [Main Release.Minor Release.BugFix]

# Imports random library
import random

# Import for file input/output and other OS functions
import os

# Spits out a random phrase to the user with question() and word()
def heySiri():
    print("Hey Siri " + question() + " is " + word() + "?")

# Uses the word.txt list and reads from the list, makes it an array and randomly chooses
# a word from the english dictionary for the user
def word():

    #Opens the words.txt file and reads it in the /english-words-master/ folder
    wlist = open("./english-words-master/words.txt").read()

    # Puts all lines of the .txt file into an array
    wline = wlist[0:]

    # Splits the text
    # like
    # this
    # for
    # example
    # Into the below array
    # ['like', 'this', 'for', 'example']
    words = wline.split()

    # Chooses a random word from the array
    randoWord = random.choice(words)

    # Returns the result to the user to use for output
    return randoWord

# Uses the 5 W's and 1 H to formulate a question to ask Siri and does the same as word()
def question():
    qlist = open("./english-words-master/phrasing.txt").read()
    qline = qlist[0:]

    phrasing = qline.split()
    randoQues = random.choice(phrasing)

    return randoQues

# Function used to repeat the code until the user quits
def repeat():
    # Yes and no array to use for
    yesChoice = ['yes', 'y']
    noChoice = ['no', 'n']

    # Asks the user a question and converts Yes / Y / No / N to lower case automatically
    # to yes / y / no / n
    prompt = input("Would you like another phrase? [Y]es [N]o ").lower()

    # An IF statement that loops when user says Y or Yes and exits and closes with N or No
    if prompt in yesChoice:
        heySiri()
        repeat()
    elif prompt in noChoice:
        exit

    # If the user enters anything else but the choices in yesChoice/noChoice it reprompts
    # the user to use [Y]es or [N]o and repeats the loop
    else:
        prompt = input("Please use choice [Y]es or [N]o ")
        if prompt in yesChoice:
            heySiri()
            repeat()
        elif prompt in noChoice:
            exit

# Calls the random phrase function
heySiri()

# Calls the repeat function
repeat()



    
