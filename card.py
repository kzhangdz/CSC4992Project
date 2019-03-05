from pygameEnvironment import *
import os.path

'''may be able to tie the card to a button
Clicking the button will change the card.'''

class CardStatus:
    '''enum for card state'''
    back, front, solved = range(3)
    # _unused, back, front, solved = range(4)

class Card:
    def __init__(self, imageDirectories, images):
        '''inititialize a card'''
        '''images: list of images (back and front)'''
        self.status = CardStatus.back
        self.cardImageDirectories = imageDirectories #use imageDirectories for comparison
        self.cardImages = images #list of images (back and front)
        #FIXME: add a pygame.Rect. This will be important in clicking.
        #See button.py for examples
        #May also add a draw and isClicked function
        #When refactoring, it may be best to derive from Button class

        imageSize = self.cardImages[CardStatus.back]
        #initialize surface and rect. How will you decide the rect position?

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def compareFrontImage(self, otherCard):
        'return true if both cards have the same front image DIRECTORY'
        'pass in Card object'
        if self.cardImageDirectories[CardStatus.front] == otherCard.cardImageDirectories[CardStatus.front]:
            return True
        else:
            return False

    def showCard(self, x, y):
        '''show card to user'''
        #USE SWITCH STATEMENT TO MEET REQUIREMENT
        if self.status == CardStatus.back:
            gameDisplay.blit(self.cardImages[0], (x,y))
        elif self.status == CardStatus.front:
            gameDisplay.blit(self.cardImages[1], (x,y))
        elif self.status == CardStatus.solved:
            pass

#test code
if __name__ == "__main__":
    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.gif')
    image = pygame.image.load(imgDirectory)
    images = [image, image]

    newCard = Card(images)
    print(CardStatus.back)
    print(CardStatus.front)
    print(CardStatus.solved)

    if newCard.status == CardStatus.back:
        print("back")

    print(newCard.cardImages)

    newCard.setStatus(CardStatus.solved)
    print(newCard.getStatus())
