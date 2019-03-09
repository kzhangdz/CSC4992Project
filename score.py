from pygameEnvironment import *
import os.path
from textPrinter import *
from constant import *

class Score:
    def __init__(self):
        self.score = 0
        self.multiplier = 0 #how many cards have been matched in a row

    def raiseMultiplier(self):
        self.multiplier += 1

    def resetMultiplier(self):
        self.multiplier = 0

    def raiseScore(self):
        'increase score'
        #FIXME: Implement a more complex algorithm
        bonus = self.multiplier * 50
        scoreAddition = 100 + bonus
        self.score = self.score + scoreAddition

    def displayMultiplier(self):
        x = DISPLAY_WIDTH * 0.15
        y = DISPLAY_HEIGHT * 0.9
        TextPrinter.displayText('Multiplier:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.3
        TextPrinter.displayText(str(self.multiplier), (x, y), 30, WHITE)

    def displayScore(self):
        x = DISPLAY_WIDTH * 0.75
        y = DISPLAY_HEIGHT * 0.1
        TextPrinter.displayText('Score:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.85
        TextPrinter.displayText(str(self.score), (x, y), 30, WHITE)

#test code
if __name__ == "__main__":
    pass
