# App: yoSiri
# Description: A bot to create randomized questions to ask Siri
# Author: Ronald Pusey
# Create Date: 5/9/2022
# Version: 0.0.1 [Main Release.Minor Release.BugFix]

import random
import os

list = open("./english-words-master/words.txt").read()
line = list[0:]

words = line.split()
randoWord = random.choice(words)

questionList = open("./english-words-master/phrasing.txt")


print(randoWord)

#word1 = 'where'
#word2 = 'Carmen San Diego'

#print("Hey Siri " + word1 + " is " + word2 + "?")