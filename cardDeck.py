from card import *
from directoryParser import *
import random
from pygameEnvironment import *
from constant import *

class CardDeck:
    '''class to load a deck of cards'''
    def __init__(self, theme, numCards):
        self.deck = CardDeck.loadCards(theme, numCards)
        self.cardCount = numCards

    def loadCards(theme, numCards):
        '''returns a list of cards'''
        #get image directories
        backDirectory = retrieveCardImages(theme, "back")
        frontDirectories = retrieveCardImages(theme, "front")
        solvedDirectory = retrieveCardImages(theme, "solved")

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

        imageDirectories = [backDirectory, neededFrontDirectories, solvedDirectory]

        #load cards
        cardList = []
        if numCards == 10:
            cardList = CardDeck.load10Cards(theme, imageDirectories)
        elif numCards == 14:
            cardList = CardDeck.load14Cards(theme, imageDirectories)
        elif numCards == 18:
            cardList = CardDeck.load18Cards(theme, imageDirectories)
        
        return cardList

    def load10Cards(theme, imageDirectories):
        #define positions
        yPosRow1 = DISPLAY_HEIGHT * 0.3 # y position of row 1 of cards
        yPosRow2 = DISPLAY_HEIGHT * 0.6 # y position of row 2 of cards
        xPos = DISPLAY_WIDTH * 0.15 #x position of first card in row

        cardList = []

        #initialize first row
        for i in range(0, 5):
            newCard = Card((xPos, yPosRow1), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.15)

        #reset xPos
        xPos = DISPLAY_WIDTH * 0.15

        #initialize second row
        for i in range(5, 10):
            newCard = Card((xPos, yPosRow2), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.15)

        return cardList

    def load14Cards(theme, imageDirectories):
        #define positions
        yPosRow1 = DISPLAY_HEIGHT * 0.3 # y position of row 1 of cards
        yPosRow2 = DISPLAY_HEIGHT * 0.6 # y position of row 2 of cards
        xPos = DISPLAY_WIDTH * 0.05 #x position of first card in row

        cardList = []

        #initialize first row
        for i in range(0, 7):
            newCard = Card((xPos, yPosRow1), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.13)

        #reset xPos
        xPos = DISPLAY_WIDTH * 0.05

        #initialize second row
        for i in range(7, 14):
            newCard = Card((xPos, yPosRow2), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.13)

        return cardList

    def load18Cards(theme, imageDirectories):
        #define positions
        yPosRow1 = DISPLAY_HEIGHT * 0.2 # y position of row 1 of cards
        yPosRow2 = DISPLAY_HEIGHT * 0.4 # y position of row 2 of cards
        yPosRow3 = DISPLAY_HEIGHT * 0.6 # y position of row 3 of cards
        xPos = DISPLAY_WIDTH * 0.07 #x position of first card in row

        cardList = []

        #initialize first row
        for i in range(0, 6):
            newCard = Card((xPos, yPosRow1), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.15)

        #reset xPos
        xPos = DISPLAY_WIDTH * 0.07

        #initialize second row
        for i in range(6, 12):
            newCard = Card((xPos, yPosRow2), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.15)

        #reset xPos
        xPos = DISPLAY_WIDTH * 0.07

        #initialize second row
        for i in range(12, 18):
            newCard = Card((xPos, yPosRow3), [imageDirectories[0][0], imageDirectories[1][i], imageDirectories[2][0]])
            cardList.append(newCard)
            xPos = xPos + (DISPLAY_WIDTH * 0.15)

        return cardList

    def checkDeckStatus(self, score):
        'analyze if cards should be switched to solved state or flipped back down'
        'scan through cards to see if two cards are flipped face up'
        'if they match, switch them to solved'
        'if not, flip them back down after WAITING'
        frontCardIndexList = [] # list of index for cards that are face up

        #find index of cards that are face up
        for i in range(len(self.deck)):
            if self.deck[i].status == CardStatus.front:
                frontCardIndexList.append(i)

        if len(frontCardIndexList) == 2: #check that exactly 2 cards are face up
            firstCardIndex = frontCardIndexList[0]
            secondCardIndex = frontCardIndexList[1]

            #if card images match, switched them to solved
            if self.deck[firstCardIndex].compareFrontImage(self.deck[secondCardIndex]):
                #display card front images
                self.deck[firstCardIndex].showCard()
                self.deck[secondCardIndex].showCard()
                pygame.display.update()

                #wait a bit
                pygame.time.wait(800)

                #update state to solved
                self.deck[firstCardIndex].setStatus(CardStatus.solved)
                self.deck[secondCardIndex].setStatus(CardStatus.solved)

                #increase score
                score.raiseMultiplier()
                score.raiseScore()
                score.displayScore()
                pygame.display.update()
            else:
                #display card front images
                self.deck[firstCardIndex].showCard()
                self.deck[secondCardIndex].showCard()
                pygame.display.update()

                #wait a bit
                pygame.time.wait(800)

                #update state to back
                self.deck[firstCardIndex].setStatus(CardStatus.back)
                self.deck[secondCardIndex].setStatus(CardStatus.back)

                #reset score multiplier
                score.resetMultiplier()

        #may need to call checkAllFaceUp function

    def checkAllFaceUp(self):
        'if all cards face up, return True and send to results screen'
        scoredCardList = []
        for card in self.deck: #add cards to list if they are solved
            if card.status == CardStatus.solved:
                scoredCardList.append(card)

        if len(scoredCardList) == self.cardCount: #if all cards are solved
            return True
        else:
            return False
        

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
        
