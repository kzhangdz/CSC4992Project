import pygame
from constant import *

'''file that sets up the pygame environment'''

#initialize pygame
pygame.init()

#set window size
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#set window name
pygame.display.set_caption('Memory Game')

#set up clock
clock = pygame.time.Clock()
