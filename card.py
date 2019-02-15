from pygameEnvironment import *
import os.path

class CardStatus:
    '''enum for card state'''
    back, front, solved = range(3)
    # _unused, back, front, solved = range(4)

class Card:
    '''def __init__(self):
        self.status = CardStatus.back
        #call directoryParser for cardImage
        imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.gif')
        self.cardImage = pygame.image.load(imgDirectory)'''

    '''def __init__(self, *args, **kwargs)'''

    def __init__(self, images):
        '''inititialize a card'''
        '''images: list of images (back and front)'''
        self.status = CardStatus.back
        self.cardImages = images #list of images (back and front)

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

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
