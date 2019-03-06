from card import *
from directoryParser import DirectoryParser
import random
from pygameEnvironment import *
from constant import *

class CardDeck:
    '''class to load a deck of cards'''
    def __init__(self, theme, numCards):
        self.deck = CardDeck.loadCards(theme, numCards)

    def loadCards(theme, numCards):
        '''returns a list of cards'''
        #get image directories
        backDirectory = DirectoryParser.retrieveCardImages(theme, "back")
        frontDirectories = DirectoryParser.retrieveCardImages(theme, "front")  

        #randomize front card image directories
        random.shuffle(frontDirectories)

        #reduce number of needed front directories
        neededFrontDirectories = []
        for i in range(numCards//2):
            neededFrontDirectories.append(frontDirectories[i])

        #double image directories so each card has a directory
        neededFrontDirectories = neededFrontDirectories + neededFrontDirectories

        #shuffle image directories again
        random.shuffle(neededFrontDirectories)

        '''#convert image directories to pygame images
        backImages = []
        frontImages = []
        for image in backDirectory:
            backImage = pygame.image.load(image)
            backImages.append(backImage)
        for image in neededFrontDirectories:
            frontImage = pygame.image.load(image)
            frontImages.append(frontImage)'''

        imageDirectories = [backDirectory, neededFrontDirectories]

        #load cards
        cardList = []
        if numCards == 10:
            cardList = CardDeck.load10Cards(theme, imageDirectories)
        elif numCards == 20:
            pass
        
        '''#create list of cards with unique images
        cardList = []
        for i in range(numCards//2):
            imgDirectories = [backDirectory[0], frontDirectories[i]]
            imgList = [backImages[0], frontImages[i]]

            newCard = card.Card(imgDirectories, imgList)
            cardList.append(newCard)'''
        
        return cardList

    def load10Cards(theme, imageDirectories):
        #define positions
        yPosRow1 = DISPLAY_HEIGHT * 0.3 # y position of row 1 of cards
        yPosRow2 = DISPLAY_HEIGHT * 0.5 # y position of row 2 of cards
        xPos = DISPLAY_WIDTH * 0.2 #x position of first card in row

        cardList = []

        #initialize first row
        for i in range(0, 5):
            newCard = Card((xPos, yPosRow1), [imageDirectories[0][0], imageDirectories[1][i]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.1)

        #reset xPos
        xPos = DISPLAY_WIDTH * 0.2

        #initialize second row
        for i in range(5, 10):
            newCard = Card((xPos, yPosRow2), [imageDirectories[0][0], imageDirectories[1][i]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.1)

        return cardList

    def checkDeckStatus(self):
        'analyze if cards should be switched to solved state or flipped back down'
        'scan through cards to see if two cards are flipped face up'
        'if they match, switch them to solved'
        'if not, flip them back down after WAITING'
        frontCardIndexList = [] # list of index for cards that are face up

        #find index of cards that are face up
        for i in range(len(self.deck)):
            if deck[i].status == CardStatus.front:
                frontCardIndexList.append(i)

        if frontCardIndexList == 2: #check that exactly 2 cards are face up
            firstCardIndex = frontCardIndexList[0]
            secondCardIndex = frontCardIndexList[1]

            #if card images match, switched them to solved
            if deck[firstCardIndex].compareFrontImage(deck[secondCardIndex]):
                #FIXME: add a wait function

                deck[firstCardIndex].setStatus(CardStatus.solved)
                deck[secondCardIndex].setStatus(CardStatus.solved)

                #FIXME: increase score
            else:
                #FIXME: add a wait function

                deck[firstCardIndex].setStatus(CardStatus.back)
                deck[secondCardIndex].setStatus(CardStatus.back)

        #may need to use showCard() function again

#test code
if __name__ == "__main__":
    deck0 = CardDeck("theme1", 10)

    #print out images and directories of first 2 cards
    print("Card 0 back image:", deck0.deck[0].cardImages[0])
    print("Card 0 front image:", deck0.deck[0].cardImages[1])
    print("Card 0 back image dir:", deck0.deck[0].cardImageDirectories[0])
    print("Card 0 front image dir:", deck0.deck[0].cardImageDirectories[1])
    print("Card 1 back image:", deck0.deck[1].cardImages[0])
    print("Card 1 front image:",deck0.deck[1].cardImages[1])
    print("Card 1 back image dir:", deck0.deck[1].cardImageDirectories[0])
    print("Card 1 front image dir:", deck0.deck[1].cardImageDirectories[1])

    #compare front images of first two cards
    if deck0.deck[0].compareFrontImage(deck0.deck[1]):
        print("Card 0 and Card 1 have the same image")
    else:
        print("Card 0 and Card 1 have diff images")

    #print all image directories used in deck
    print("List of Front Images")
    for item in deck0.deck:
        print(item.cardImageDirectories[CardStatus.front])
        
