from pygameEnvironment import *
import os.path
#from constant import DISPLAY_WIDTH, DISPLAY_HEIGHT

'''may be able to tie the card to a button
Clicking the button will change the card.'''
#FIXME: When refactoring, it may be best to derive from Button class

class CardStatus:
    '''enum for card state'''
    back, front, solved = range(3)
    # _unused, back, front, solved = range(4)

class Card:
    imageDimensions = (87, 115)
    #imageDimensions = (DISPLAY_WIDTH*0.10875, DISPLAY_HEIGHT*0.2)

    def __init__(self, pos, imageDirectories):
        '''inititialize a card'''
        '''imageDirectories: list of image directories (back, front, solved)'''
        self.status = CardStatus.back
        self.cardImageDirectories = imageDirectories #use imageDirectories for comparison
        self.cardImages = self.loadCardImages(imageDirectories) #list of images (back, front, solved)
        self.position = pos

        self.surf = pygame.Surface(Card.imageDimensions, pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(self.position, Card.imageDimensions)

        self.surf.blit(self.cardImages[CardStatus.back], self.rect)

    def loadCardImages(self, imageDirectories):
        #load images
        backImage = pygame.image.load(imageDirectories[CardStatus.back])
        frontImage = pygame.image.load(imageDirectories[CardStatus.front])
        solvedImage = pygame.image.load(imageDirectories[CardStatus.solved])

        #scale images to correct size
        backImage = pygame.transform.scale(backImage, Card.imageDimensions)
        frontImage = pygame.transform.scale(frontImage, Card.imageDimensions)
        solvedImage = pygame.transform.scale(solvedImage, Card.imageDimensions)

        #store images in list
        imageList = [backImage, frontImage, solvedImage]
        return imageList

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def switchStatus(self):
        if self.status == CardStatus.back:
            self.setStatus(CardStatus.front)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

    def compareFrontImage(self, otherCard):
        'return true if both cards have the same front image DIRECTORY'
        'pass in Card object'
        if self.cardImageDirectories[CardStatus.front] == otherCard.cardImageDirectories[CardStatus.front]:
            return True
        else:
            return False

    def showCard(self):
        '''show card to user'''
        #USE SWITCH STATEMENT TO MEET REQUIREMENT
        if self.status == CardStatus.back:
            gameDisplay.blit(self.surf, self.rect)
            gameDisplay.blit(self.cardImages[CardStatus.back], self.position)
        elif self.status == CardStatus.front:
            gameDisplay.blit(self.surf, self.rect)
            gameDisplay.blit(self.cardImages[CardStatus.front], self.position)
        elif self.status == CardStatus.solved:
            gameDisplay.blit(self.surf, self.rect)
            gameDisplay.blit(self.cardImages[CardStatus.solved], self.position)

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
