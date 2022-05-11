# App: yoSiri
# Description: A bot to create randomized questions to ask Siri
# Author: Ronald Pusey
# Create Date: 5/9/2022
# Version: 0.0.1 [Main Release.Minor Release.BugFix]

import random
import os

def heySiri():
    print("Hey Siri " + question() + " is " + word() + "?")

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

yesChoice = ['yes','y']
noChoice = ['no', 'n']

def repeat():
    prompt = input("Would you like another phrase? [Y]es [N]o ").lower()
    if prompt in yesChoice:
        heySiri()
        repeat()
    elif prompt in noChoice:
        exit
    else:
        print("[Y]es or [N]o ")
        repeat()

heySiri()
repeat()





#while True:
#    heySiri()
#    cont = input("Would you like another phrase? [Y]es or [N]o: ")
#    while cont.lower() not in ("yes","y","no","n"):
#        cont = input("Would you like another phrase? [Y]es or [N]o: ")
#    if cont == "no" or "n":
#        break

#def yes_or_no(question, yourFunction):
#    reply = str(input(question+' ([Y]es | [N]o): ')).lower().strip()
#    if reply == 'y' or 'yes':
#        yourFunction
#    elif reply == 'n' or 'no':
#        exit
#    else:
#        return yes_or_no("Please Enter ([Y]es | [N]o ")

#yes_or_no("Would you like another phrase", heySiri())

#print(word())
#print(question())




#heySiri()

#while True:
    #yes_or_no("Would you like another phrase? [Y]es | [N]o: `n")
    #heySiri()



    
