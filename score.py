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

class MultiplayerScore(Score):
    def __init__(self):
        super(MultiplayerScore, self).__init__()
        self.score2 = 0
        self.multiplier2 = 0
        
    def raiseMultiplier2(self):
        self.multiplier2 += 1

    def resetMultiplier2(self):
        self.multiplier2 = 0

    def raiseScore2(self):
        'increase score'
        bonus = self.multiplier2 * 50
        scoreAddition = 100 + bonus
        self.score2 = self.score2 + scoreAddition

    def displayMultiplier(self):
        #multiplier 1
        x = DISPLAY_WIDTH * 0.13
        y = DISPLAY_HEIGHT * 0.85
        TextPrinter.displayText('Multiplier 1:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.3
        TextPrinter.displayText(str(self.multiplier), (x, y), 30, WHITE)

        #multiplier 2
        x = DISPLAY_WIDTH * 0.13
        y = DISPLAY_HEIGHT * 0.95
        TextPrinter.displayText('Multiplier 2:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.3
        TextPrinter.displayText(str(self.multiplier2), (x, y), 30, WHITE)

    '''def displayMultiplier2(self):
        x = DISPLAY_WIDTH * 0.13
        y = DISPLAY_HEIGHT * 0.9
        TextPrinter.displayText('Multiplier 2:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.3
        TextPrinter.displayText(str(self.multiplier2), (x, y), 30, WHITE)'''

    def displayScore(self):
        #score 1
        x = DISPLAY_WIDTH * 0.73
        y = DISPLAY_HEIGHT * 0.05
        TextPrinter.displayText('Score 1:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.85
        TextPrinter.displayText(str(self.score), (x, y), 30, WHITE)

        #score 2
        x = DISPLAY_WIDTH * 0.73
        y = DISPLAY_HEIGHT * 0.15
        TextPrinter.displayText('Score 2:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.85
        TextPrinter.displayText(str(self.score2), (x, y), 30, WHITE)

    '''def displayScore2(self):
        x = DISPLAY_WIDTH * 0.73
        y = DISPLAY_HEIGHT * 0.2
        TextPrinter.displayText('Score 2:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.85
        TextPrinter.displayText(str(self.score2), (x, y), 30, WHITE)'''

#test code
if __name__ == "__main__":
    pass
