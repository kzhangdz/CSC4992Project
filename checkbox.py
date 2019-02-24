import pygame
from pygameEnvironment import *
import os
from button import ImageButton

trueImageDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'checkbox_true.png')
falseImageDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_test.png')


class Checkbox(ImageButton):
    '''def __init__(self, position, imageDirectory, trueFalseState):
        super().__init__(self, position, imageDirectory)
        self.state = trueFalseState'''

    #trueImageDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'checkbox_true.png')
    #falseImageDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_test.png')

    def __init__(self, position, imageDirectory=falseImageDirectory):
        ImageButton.__init__(self, position, imageDirectory)

        self.pos = position
        self.state = False
        if imageDirectory == trueImageDirectory:
            self.state = True

    def switchState(self):
        if self.state == True:
            self.state = False
            #newCheckbox = Checkbox(self.pos, falseImageDirectory)
            #self = newCheckbox
            imageFile = pygame.image.load(falseImageDirectory)
            imageRect = imageFile.get_rect()
            imageRect.center = self.rect.center
            self.image.blit(imageFile, imageRect)
            self.draw(gameDisplay)
            pygame.display.update()
            print(self.state)
        elif self.state == False:
            self.state = True
            #newCheckbox = Checkbox(self.pos, trueImageDirectory)
            #self = newCheckbox
            imageFile = pygame.image.load(trueImageDirectory)
            imageRect = imageFile.get_rect()
            imageRect.center = self.rect.center
            self.image.blit(imageFile, imageRect)
            self.draw(gameDisplay)
            pygame.display.update()
            print(self.state)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #self.switchState()
                #self.draw(gameDisplay)
                #pygame.display.update()
                return self.rect.collidepoint(event.pos)

if __name__ == "__main__":
    newCheckbox = Checkbox((100, 100))
    gameDisplay.fill(FOREST_GREEN)
    newCheckbox.draw(gameDisplay)

    pygame.display.update()
