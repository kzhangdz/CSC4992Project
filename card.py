from pygameEnvironment import *
import os.path
from button import ImageButton

'''may be able to tie the card to a button
Clicking the button will change the card.'''

class CardStatus:
    '''enum for card state'''
    back, front, solved = range(3)
    # _unused, back, front, solved = range(4)

class Card(ImageButton):
    def __init__(self, position, imageDirectories, state):
        'pass in list of image directories, one for each card state'
        'state: CardStatus variable'
        self.status = state
        self.cardImageDirectories = imageDirectories

        #choose image directory based on state
        currentImageDirectory = self.cardImageDirectories[self.status]

        ImageButton.__init__(self, position, currentImageDirectory)                

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

#test code
if __name__ == "__main__":
    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.gif')
    imgDirectories = [imgDirectory, imgDirectory]

    newCard = Card((200, 200), imgDirectories, CardStatus.back)
    print(CardStatus.back)
    print(CardStatus.front)
    print(CardStatus.solved)

    if newCard.status == CardStatus.back:
        print("back")

    newCard.setStatus(CardStatus.solved)
    print(newCard.getStatus())
