import pygame
from pygameEnvironment import *
import os

#button class from:
#https://stackoverflow.com/questions/47981842/how-do-i-create-a-pygame-with-multiple-menus

class Button:
    
    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

class ImageButton(Button):
    def __init__(self, position, imageDirectory):
        imageFile = pygame.image.load(imageDirectory)

        #tie pygame.Surface to pygame.image
        #get image size
        size = imageFile.get_rect().size

        #make surface and rect the same size as image
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32) #SRCALPHA and 32 set transparent surface
        self.rect = pygame.Rect((0,0), size)

        imageRect = imageFile.get_rect()
        imageRect.center = self.rect.center

        self.image.blit(imageFile, imageRect)

        # set after centering text
        self.rect.center = position
            
'''class ImageButton:
    def __init__(self, position, imageDirectory):
        imageFile = pygame.image.load(imageDirectory)

        #tie pygame.Surface to pygame.image
        #get image size
        size = imageFile.get_rect().size

        #make surface and rect the same size as image
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32) #SRCALPHA and 32 set transparent surface
        self.rect = pygame.Rect((0,0), size)

        imageRect = imageFile.get_rect()
        imageRect.center = self.rect.center

        self.image.blit(imageFile, imageRect)

        # set after centering text
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)'''

if __name__ == "__main__":
    #imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button.png')
    imgDirectory = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'button_test.png')
    
    newButton = ImageButton((100, 100), imgDirectory)
    gameDisplay.fill(FOREST_GREEN)
    newButton.draw(gameDisplay)

    pygame.display.update()

