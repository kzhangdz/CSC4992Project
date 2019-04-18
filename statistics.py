from card import *
from directoryParser import *
import random
from textPrinter import *
from pygameEnvironment import *
from constant import *

class Statistics:
    def __init__(self):
        self.CardsClicked = 0
        self.CardsMatched = 0
        self.GamesPlayed = 0


    def raiseCardsClicked(self):
        self.CardsClicked = self.CardsClicked + 1

    def raiseCardsMatched(self):
        self.CardsMatched = self.CardsMatched + 1

    def raiseGamesPlayed(self):
        self.GamesPlayed = self.GamesPlayed + 1

    def displayStats(self):
        x = DISPLAY_WIDTH * 0.25
        y = DISPLAY_HEIGHT * 0.4
        TextPrinter.displayText('Clicks:', (x, y), 30, BLACK)

        x = DISPLAY_WIDTH * 0.35
        TextPrinter.displayText(str(self.CardsClicked), (x, y), 30, BLACK)

        a = DISPLAY_WIDTH * 0.27
        b = DISPLAY_HEIGHT * 0.5
        TextPrinter.displayText('Matched:', (a, b), 30, BLACK)

        a = DISPLAY_WIDTH * 0.37
        TextPrinter.displayText(str(self.CardsMatched), (a, b), 30, BLACK)

        c = DISPLAY_WIDTH * 0.25
        d = DISPLAY_HEIGHT * 0.6
        TextPrinter.displayText('Played:', (c, d), 30, BLACK)

        c = DISPLAY_WIDTH * 0.35
        TextPrinter.displayText(str(self.GamesPlayed), (c, d), 30, BLACK)

    def list_dict():
        ages = {}

        ages['Sue'] = 23
        ages['Peter'] = 19
        ages['Andrew'] = 78
        ages['Karren'] = 45

        #Use the function has_key() -
        #This function takes this form:
        #function_name.has_key(key-name)
        #It returns TRUE
        #if the dictionary has key-name in it
        #but returns FALSE if it doesn't.
        #Remember - this is how 'if' statements work -
        #they run if something is true
        #and they don't when something is false.
        if ages.has_key('Sue'):
            print("Sue is in the dictionary. She is", \
        ages['Sue'], "years old")

        else:
            print("Sue is not in the dictionary")

        #Use the function keys() -
        #This function returns a list
        #of all the names of the keys.
        #E.g.
        print("The following people are in the dictionary:")
        print(ages.keys())

        #You could use this function to
        #put all the key names in a list:
        keys = ages.keys()

        #You can also get a list
        #of all the values in a dictionary.
        #You use the values() function:
        print("People are aged the following:", \
        ages.values())

        #Put it in a list:
        values = ages.values()

        #You can sort lists, with the sort() function
        #It will sort all values in a list
        #alphabetically, numerically, etc...
        #You can't sort dictionaries -
        #they are in no particular order
        print(keys)
        keys.sort()
        print(keys)

        print(values)
        values.sort()
        print(values)

        #You can find the number of entries
        #with the len() function:
        print("The dictionary has", \
        len(ages), "entries in it")
