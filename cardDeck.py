from card import *
from constant import *
from directoryParser import DirectoryParser
import random
from pygameEnvironment import *

class CardDeck:
    '''class to load a deck of cards'''
    def __init__(self, theme, numCards):
        self.deck = CardDeck.loadCards(theme, numCards)

    def loadCards(theme, numCards):
        '''returns a list of cards'''
        #get image directories. Each variable is a list
        backDirectory = DirectoryParser.retrieveCardImages(theme, "back")
        frontDirectories = DirectoryParser.retrieveCardImages(theme, "front")
        solvedDirectory = DirectoryParser.retrieveCardImages(theme, "solved")

        #randomize front card images
        random.shuffle(frontDirectories)

        #create list of cards with unique images
        cardList = []
        for i in range(numCards//2): #only go up to half, b/c each card needs a pair
            #FIXME: need a way to pass in varying position
            newCard = card.Card(, [backDirectory[0], frontDirectories[i], solvedDirectory[0]], CardStatus.back)
            cardList.append(newCard)

        #double card list so each card has a pair
        cardList = cardList + cardList

        #randomize card list
        random.shuffle(cardList)
        
        return cardList

#test code
if __name__ == "__main__":
    deck1 = CardDeck("theme1", 2)
    print(deck1.deck)
    print(deck1.deck[0])
