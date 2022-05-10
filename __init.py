# App: yoSiri
# Description: A bot to create randomized questions to ask Siri
# Author: Ronald Pusey
# Create Date: 5/9/2022
# Version: 0.0.1 [Main Release.Minor Release.BugFix]

import random
import os


def word():
    wlist = open("./english-words-master/words.txt").read()
    wline = wlist[0:]

    words = wline.split()
    randoWord = random.choice(words)

    return randoWord

def question():
    qlist = open("./english-words-master/phrasing.txt").read()
    qline = qlist[0:]

    phrasing = qline.split()
    randoQues = random.choice(phrasing)

    return randoQues




#print(word())
#print(question())

print("Hey Siri " + question() + " is " + word() + "?")