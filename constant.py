'''important constants for pygame'''

import pygame
from button import Button
from button import ImageButton
from directoryParser import *
import math


#declare frames per second
FPS = 30

#declare size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#declare text sizes
TITLE_SIZE = 100

#declare text positions
TITLE_X = DISPLAY_WIDTH * 0.5
TITLE_Y = DISPLAY_HEIGHT * 0.15

#declare colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
FOREST_GREEN = (34,139,34)

# screen positions
top_left = (DISPLAY_WIDTH * 0.07, DISPLAY_HEIGHT * 0.07)
bottom_right = (DISPLAY_WIDTH * 0.9, DISPLAY_HEIGHT * 0.9)

# icon sizes: where it is, actual image, scaled image
	# options
imgDirectoryOptions = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'hamburger.png')
hamburger_icon = pygame.image.load(imgDirectoryOptions)
hamburger_icon = pygame.transform.scale(hamburger_icon, (math.floor(DISPLAY_WIDTH * 0.11), math.floor(DISPLAY_HEIGHT * 0.15)))
optionsButton = ImageButton(bottom_right, imageFile = hamburger_icon)
	# back
imgDirectoryBack = os.path.join(os.path.abspath(os.curdir), 'images', 'menu', 'back_button2.png')
back_arrow = pygame.image.load(imgDirectoryBack)
back_arrow = pygame.transform.scale(back_arrow, (math.floor(DISPLAY_WIDTH * 0.15), math.floor(DISPLAY_HEIGHT * 0.1)))
backButton = ImageButton(top_left, imageFile = back_arrow)