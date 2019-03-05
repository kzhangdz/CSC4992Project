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
            imgDirectories = [backDirectory[0], frontDirectories[i]]
            imgList = [backImages[0], frontImages[i]]

            newCard = card.Card(imgDirectories, imgList)
            cardList.append(newCard)

        #double card list so each card has a pair
        cardList = cardList + cardList

        #randomize card list
        random.shuffle(cardList)
        
        return cardList

#test code
if __name__ == "__main__":
    deck1 = CardDeck("theme1", 4)
    print(deck1.deck)

    #print out images and directories of first 2 cards
    print("Card 0 back image:", deck1.deck[0].cardImages[0])
    print("Card 0 front image:", deck1.deck[0].cardImages[1])
    print("Card 0 back image dir:", deck1.deck[0].cardImageDirectories[0])
    print("Card 0 front image dir:", deck1.deck[0].cardImageDirectories[1])
    print("Card 1 back image:", deck1.deck[1].cardImages[0])
    print("Card 1 front image:",deck1.deck[1].cardImages[1])
    print("Card 1 back image dir:", deck1.deck[1].cardImageDirectories[0])
    print("Card 1 front image dir:", deck1.deck[1].cardImageDirectories[1])

    #compare front images of first two cards
    if deck1.deck[0].compareFrontImage(deck1.deck[1]):
        print("Card 0 and Card 1 have the same image")
    else:
        print("Card 0 and Card 1 have diff images")

    #print all image directories used in deck
    print("List of Images")
    for item in deck1.deck:
        print(item.cardImageDirectories[card.CardStatus.front])
        
