import pygame
from constant import *
from pygameEnvironment import *

class TextPrinter:
    '''used to display messages on menus'''
    
    def __init__(self):
        pass

    def textObjects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    @staticmethod
    def displayTitle(text):
        '''displays title texts'''
        largeText = pygame.font.Font('freesansbold.ttf', TITLE_SIZE)
        textSurface, textRectangle = TextPrinter.textObjects(text, largeText, BLACK)
        textRectangle.center = (TITLE_X, TITLE_Y)
        gameDisplay.blit(textSurface, textRectangle)

        #pygame.display.update()
