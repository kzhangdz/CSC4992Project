from pygameEnvironment import *
import os.path
from textPrinter import *
from constant import *

class Score:
    def __init__(self):
        self.score = 0

    def raiseScore(self):
        'increase score'
        #FIXME: Implement a more complex algorithm
        self.score += 100

    def displayScore(self):
        x = DISPLAY_WIDTH * 0.75
        y = DISPLAY_HEIGHT * 0.1
        TextPrinter.displayText('Score:', (x, y), 30, WHITE)

        x = DISPLAY_WIDTH * 0.85
        TextPrinter.displayText(str(self.score), (x, y), 30, WHITE)

#test code
if __name__ == "__main__":
    pass
