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
