from random import randint
import csv
import os
import sys

#import curses

# return list of words
def getWords(filename):
    out = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            out.append(row)
    return out

fp = sys.argv[1]
words = getWords(fp);

while(True):
    pin = words[randint(0, len(words)-1)]
    print("")
    input(pin['pin'])
    print(" ")
    input(pin['character'])

    os.system('clear') 
