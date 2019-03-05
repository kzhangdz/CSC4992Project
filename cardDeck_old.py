import card
from directoryParser import DirectoryParser
import random
from pygameEnvironment import *

class CardDeck:
    '''class to load a deck of cards'''
    def __init__(self, theme, numCards):
        self.deck = CardDeck.loadCards(theme, numCards)

    def loadCards(theme, numCards):
        '''returns a list of cards'''
        #get image directories
        backDirectory = DirectoryParser.retrieveCardImages(theme, "back")
        frontDirectories = DirectoryParser.retrieveCardImages(theme, "front")

        #convert image directories to pygame images
        backImages = []
        frontImages = []
        for image in backDirectory:
            backImage = pygame.image.load(image)
            backImages.append(backImage)
        for image in frontDirectories:
            frontImage = pygame.image.load(image)
            frontImages.append(frontImage)

        #randomize front card images
        random.shuffle(frontImages)

        #create list of cards with unique images
        cardList = []
        for i in range(numCards//2):
            newCard = card.Card([backImages[0], frontImages[i]])
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
    print("Card 0 back image:", deck1.deck[0].cardImages[0])
    print("Card 0 front image:", deck1.deck[0].cardImages[1])    
    print("Card 1 back image:", deck1.deck[1].cardImages[0])
    print("Card 1 front image:",deck1.deck[1].cardImages[1])
