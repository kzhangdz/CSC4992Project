import pygame
from pygameEnvironment import *

#button class from:
#https://stackoverflow.com/questions/47981842/how-do-i-create-a-pygame-with-multiple-menus

class Button:
    
    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)
